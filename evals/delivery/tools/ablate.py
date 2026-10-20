#!/usr/bin/env python3
"""Delete each sentence of delivering-pitches in turn and report which ones no grader needs.

    python3 evals/delivery/tools/ablate.py [--paragraphs] [--runs N] [--parallel N] [--only <n,n,...>] [--list] [--json out.json]

The skill is cut into units: one sentence of a paragraph or list item, or with --paragraphs one
paragraph or list item. For each unit the skill is rewritten without it, histories are rebuilt,
the cases its section touches (CASES) run, and every grader is held to its bar (shape-* 5/5, content-* 4/5 at 5 runs, scaled
for other run counts). A unit is earned when deleting it drops some grader below its bar; the
rest are candidates to delete (ADR-0004). A unit naming a feature in EXCEPTIONS is a bounded
exception (ADR-0005): no eval can observe the feature, so it is never cut.

Each unit runs in its own copy of the repo under $TMPDIR, so units run in parallel and the
working tree is never touched.
"""
import argparse
import json
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "plugins" / "delivery" / "skills" / "delivering-pitches" / "SKILL.md"
# The cases each section of the skill can fail; a unit runs only its section's cases.
CASES = {
    "": ["s1-intake", "s1-build"],
    "Intake": ["s1-intake", "s3-epic"],
    "Designing": ["s1-intake", "s3-small"],
    "Planning": ["s1-plan", "s2-plan", "s10-plan", "s3-small"],
    "Building slices": ["s1-build", "s4-build"],
    "Proving changes": ["s1-build", "s1-gate", "s7-build", "s8-build"],
    "Shipping PRs": ["s1-pr", "s5-pr", "s9-pr"],
}
EXCEPTIONS = ("EnterPlanMode", "ExitPlanMode", "Artifact tool", "task-list tool")
SENTENCE_END = re.compile(r"(?<=[.!?:])\s+(?=[A-Z`*(\"])")


def units(body, paragraphs=False):
    """Units of `body`, each a list of (line, start, end) spans plus its section: one sentence per
    unit, or with `paragraphs` every sentence of one line (a paragraph or list item). Headings are
    never cut, nor are sentences naming an exception."""
    lines, out, section = body.splitlines(), [], ""
    for i, line in enumerate(lines):
        text = line.strip()
        if not text:
            continue
        if text.startswith("#"):
            section = text.lstrip("# ").strip()
            continue
        lead = len(line) - len(line.lstrip(" -*0123456789.")) if re.match(r"\s*([-*]|\d+\.)\s", line) else 0
        spans, start = [], lead
        if not text.startswith(("```", "|")):
            for m in SENTENCE_END.finditer(line, lead):
                spans.append((i, start, m.start()))
                start = m.end()
        spans.append((i, start, len(line)))
        spans = [sp for sp in spans if not any(e in line[sp[1]:sp[2]] for e in EXCEPTIONS)]
        groups = [spans] if paragraphs else [[sp] for sp in spans]
        out += [(g, section) for g in groups if g]
    return out


def without(lines, unit):
    out = list(lines)
    for i, a, b in sorted(unit[0], key=lambda sp: -sp[1]):
        out[i] = out[i][:a] + out[i][b:]
    return "\n".join(l for l in out if l.strip(" -*0123456789.") or not l.strip()) + "\n"


def text_of(lines, unit):
    return " ".join(lines[i][a:b].strip() for i, a, b in unit[0])


def bar(name, runs):
    return runs if name.startswith("shape-") else max(1, runs - (runs // 5))


def below_bar(result_paths, runs):
    failed = []
    cases = [c for p in result_paths if p.exists() for c in json.load(open(p))["cases"]]
    if len(cases) < len(result_paths):
        failed.append("(a case produced no result)")
    for case in cases:
        counts = {}
        for run in case["arms"]["with"]:
            for g in run["graders"]:
                counts[g["name"]] = counts.get(g["name"], 0) + bool(g["passed"])
        failed += [f'{case["name"]}/{n}' for n, c in counts.items() if c < bar(n, runs)]
    return failed


def run_cases(cases, runs, outdir, root):
    """Runs each case as its own eval in `root`, all at once (--case takes one glob). Returns the result paths."""
    procs, outs = [], []
    for case in cases:
        out = outdir / f"{case}.json"
        out.unlink(missing_ok=True)
        cmd = ["claude", "plugin", "eval", ".", "--eval-dir", "evals/delivery", "--case", case, "--model", "claude-opus-5-5",
               "--judge-model", "claude-opus-5-5", "--ablation", "none", "--scaffold", "--allow-tools", "Write", "Edit",
               "Bash", "--runs", str(runs), "-j", "5", "--trust-plugin", "--no-publish", "--json", str(out)]
        procs.append(subprocess.Popen(cmd, cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
        outs.append(out)
    for p in procs:
        p.wait()
    return outs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paragraphs", action="store_true")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--only", help="comma-separated unit numbers, as listed by --list")
    ap.add_argument("--list", action="store_true", help="print the units and exit")
    ap.add_argument("--json")
    args = ap.parse_args()

    original = SKILL.read_text(encoding="utf-8")
    head, body = re.match(r"(---\n.*?\n---\n)(.*)", original, re.S).groups()
    lines = body.splitlines()
    spans = units(body, args.paragraphs)
    if args.list:
        for n, unit in enumerate(spans, 1):
            print(f"{n:3}  [{unit[1] or 'intro'}] {text_of(lines, unit)[:110]}")
        return
    chosen = [int(n) for n in args.only.split(",") if n.strip()] if args.only else range(1, len(spans) + 1)

    def ablate(n):
        unit, section = spans[n - 1], spans[n - 1][1]
        copy = Path(tempfile.mkdtemp(prefix=f"ablate-{n}-"))
        shutil.copytree(ROOT, copy, dirs_exist_ok=True, symlinks=True,
                        ignore=shutil.ignore_patterns(".git", ".eval-deps", "results", "00000000-*"))
        # A copy, not a symlink: the runner only loads plugins from inside the directory it runs in.
        shutil.copytree(ROOT / ".eval-deps", copy / ".eval-deps", ignore=shutil.ignore_patterns(".git"))
        (copy / SKILL.relative_to(ROOT)).write_text(head + without(lines, unit), encoding="utf-8")
        subprocess.run([sys.executable, str(copy / "evals/delivery/tools/rebuild_histories.py")], cwd=copy,
                       check=True, stdout=subprocess.DEVNULL)
        dropped = below_bar(run_cases(CASES[section], args.runs, copy, copy), args.runs)
        shutil.rmtree(copy, ignore_errors=True)
        print(f"{n:3} {'earned' if dropped else 'DELETE'}  {text_of(lines, unit)[:90]}", flush=True)
        return {"unit": n, "section": section, "text": text_of(lines, unit), "earned": bool(dropped), "dropped": dropped}

    with ThreadPoolExecutor(args.parallel) as pool:
        report = sorted(pool.map(ablate, chosen), key=lambda r: r["unit"])
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Delete each sentence of delivering-pitches in turn and report which ones no grader needs.

    python3 evals/delivery/tools/ablate.py [--case <glob>] [--runs N] [--only <n,n,...>] [--json out.json]

The skill is cut into units: one sentence of a paragraph or list item, or a whole line for a
heading or code line. For each unit the skill is rewritten without it, histories are rebuilt,
the cases run, and every grader is held to its bar (shape-* 5/5, content-* 4/5 at 5 runs, scaled
for other run counts). A unit is earned when deleting it drops some grader below its bar; the
rest are candidates to delete (ADR-0004). A unit naming a feature in EXCEPTIONS is a bounded
exception (ADR-0005): no eval can observe the feature, so it is never cut.

The skill file is restored and histories rebuilt when the run ends, however it ends.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "plugins" / "delivery" / "skills" / "delivering-pitches" / "SKILL.md"
REBUILD = [sys.executable, str(Path(__file__).with_name("rebuild_histories.py"))]
EXCEPTIONS = ("EnterPlanMode", "ExitPlanMode", "Artifact tool", "task-list tool")
SENTENCE_END = re.compile(r"(?<=[.!?:])\s+(?=[A-Z`*(\"])")


def units(body):
    """(line index, start, end) spans in `body`'s lines, one per sentence or structural line."""
    spans = []
    for i, line in enumerate(body.splitlines()):
        text = line.strip()
        if not text:
            continue
        if text.startswith(("#", "```", "|")):
            spans.append((i, 0, len(line)))
            continue
        lead = len(line) - len(line.lstrip(" -*0123456789.")) if re.match(r"\s*([-*]|\d+\.)\s", line) else 0
        start = lead
        for m in SENTENCE_END.finditer(line, lead):
            spans.append((i, start, m.start()))
            start = m.end()
        spans.append((i, start, len(line)))
    return [s for s in spans if not any(e in body.splitlines()[s[0]][s[1]:s[2]] for e in EXCEPTIONS)]


def without(lines, span):
    i, a, b = span
    out = list(lines)
    line = out[i][:a] + out[i][b:]
    out[i] = line if line.strip(" -*0123456789.") else None
    return "\n".join(l for l in out if l is not None) + "\n"


def bar(name, runs):
    return runs if name.startswith("shape-") else max(1, runs - (runs // 5))


def below_bar(result_path, runs):
    failed = []
    for case in json.load(open(result_path))["cases"]:
        counts = {}
        for run in case["arms"]["with"]:
            for g in run["graders"]:
                counts[g["name"]] = counts.get(g["name"], 0) + bool(g["passed"])
        failed += [f'{case["name"]}/{n}' for n, c in counts.items() if c < bar(n, runs)]
    return failed


def run_suite(case, runs, out):
    cmd = ["claude", "plugin", "eval", ".", "--eval-dir", "evals/delivery", "--model", "claude-opus-5-5",
           "--judge-model", "claude-opus-5-5", "--ablation", "none", "--scaffold", "--allow-tools", "Write", "Edit",
           "Bash", "--runs", str(runs), "-j", "8", "--trust-plugin", "--no-publish", "--json", str(out)]
    if case:
        cmd[4:4] = ["--case", case]
    subprocess.run(cmd, cwd=ROOT, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case")
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--only", help="comma-separated unit numbers, as listed by --list")
    ap.add_argument("--list", action="store_true", help="print the units and exit")
    ap.add_argument("--json")
    args = ap.parse_args()

    original = SKILL.read_text(encoding="utf-8")
    head, body = re.match(r"(---\n.*?\n---\n)(.*)", original, re.S).groups()
    lines = body.splitlines()
    spans = units(body)
    if args.list:
        for n, (i, a, b) in enumerate(spans, 1):
            print(f"{n:3}  {lines[i][a:b].strip()}")
        return
    chosen = [int(n) for n in args.only.split(",")] if args.only else range(1, len(spans) + 1)

    report = []
    try:
        with tempfile.TemporaryDirectory() as tmp:
            for n in chosen:
                i, a, b = spans[n - 1]
                SKILL.write_text(head + without(lines, spans[n - 1]), encoding="utf-8")
                subprocess.run(REBUILD, cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
                out = Path(tmp) / f"unit-{n}.json"
                run_suite(args.case, args.runs, out)
                dropped = below_bar(out, args.runs) if out.exists() else ["(run produced no result)"]
                report.append({"unit": n, "text": lines[i][a:b].strip(), "earned": bool(dropped), "dropped": dropped})
                print(f"{n:3} {'earned' if dropped else 'DELETE'}  {lines[i][a:b].strip()[:90]}", flush=True)
    finally:
        SKILL.write_text(original, encoding="utf-8")
        subprocess.run(REBUILD, cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    sys.exit(0)


if __name__ == "__main__":
    main()

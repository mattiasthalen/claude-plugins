#!/usr/bin/env python3
"""Read a `claude plugin eval --json` result and report it by tier, stage and case.

    python3 evals/delivery/tools/report.py <result.json> [--runs]

Graders are tiered by file name: `shape-*` graders are deterministic, and a miss reads as
"add a line"; `content-*` graders are judged. This prints pass counts per tier for each stage
(from the case tags) and for each case, the graders that missed, each case's cost, and every run
that errored before it could be graded — an errored run is a failure, never a silent zero. With
--runs it also prints each run's error and trace path, which is where a failure is read before
it is trusted.

It refuses to report when the run was not judged by the calibrated judge or did not pin the
agent model, because content scores mean nothing against an uncalibrated judge.
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

CALIBRATED_JUDGE = "claude-opus-5-5"
PINNED_AGENT = "claude-opus-5-5"
args = sys.argv[1:]
if not args:
    sys.exit(__doc__)
result = json.load(open(args[0]))
show_runs = "--runs" in args
suite = result.get("suite", {})
judge, agent = suite.get("judgeModel"), suite.get("modelOverride")
if judge != CALIBRATED_JUDGE:
    sys.exit(f"judged by {judge!r}, not {CALIBRATED_JUDGE}: content scores are uncalibrated. Rerun with --judge-model {CALIBRATED_JUDGE}.")
if agent != PINNED_AGENT:
    sys.exit(f"agent model {agent!r}, not {PINNED_AGENT}: results are not comparable with the baseline.")


def tier(name):
    return "shape" if name.startswith("shape-") else "content" if name.startswith("content-") else "untiered"


def counts():
    return defaultdict(lambda: [0, 0])


by_part, lines, errored = defaultdict(counts), [], 0
print(f"claude {result.get('claudeVersion')}  judge {judge}  agent {agent}  total ${result.get('costUsd', 0):.2f}"
      + ("  PARTIAL: " + str(result.get("partialReason")) if result.get("partial") else ""))
for case in result["cases"]:
    prompt = Path(suite.get("root", ".")) / case.get("dir", "") / "prompt.md"
    head = prompt.read_text(encoding="utf-8").split("---")[1] if prompt.exists() else ""
    tags = re.search(r"^tags:\s*\[(.*?)\]", head, re.M)
    parts = [t.strip() for t in tags.group(1).split(",") if t.strip().startswith("stage-")] if tags else []
    parts = parts or ["untagged"]
    for arm, runs in case.get("arms", {}).items():
        c, misses, errs = counts(), defaultdict(int), []
        for i, run in enumerate(runs):
            if run.get("error") or not run.get("graders"):
                errs.append(i)
                continue
            for g in run["graders"]:
                if not g.get("scored", True):
                    continue
                t = tier(g["name"])
                c[t][1] += 1
                c[t][0] += bool(g["passed"])
                for p in parts:
                    by_part[p][t][1] += 1
                    by_part[p][t][0] += bool(g["passed"])
                if not g["passed"]:
                    misses[g["name"]] += 1
        errored += len(errs)
        cost = sum(r.get("costUsd", 0) for r in runs)
        tiers = "  ".join(f"{t} {p}/{n}" for t, (p, n) in sorted(c.items()))
        label = case["name"] + ("" if arm == "with" else f" [{arm}]")
        lines.append(f"{label:<28} {tiers}  runs {len(runs)}  ${cost:.2f}")
        if errs:
            lines.append(f"    ⚠ {len(errs)} run(s) errored before grading: {runs[errs[0]].get('error')}")
        for name, n in sorted(misses.items()):
            lines.append(f"    ✘ {name} ×{n}")
        if show_runs:
            for i, run in enumerate(runs):
                lines.append(f"    run {i}: score {run.get('score', 0):.2f} turns {run.get('turns')} "
                             f"err {run.get('error')} trace {run.get('tracePath')}")
for part in sorted(by_part):
    print(f"{part:<10} " + "  ".join(f"{t} {p}/{n} ({p / n:.0%})" for t, (p, n) in sorted(by_part[part].items()) if n))
if errored:
    print(f"⚠ {errored} run(s) errored before grading; they count as failures.")
print()
print("\n".join(lines))
sys.exit(1 if errored else 0)

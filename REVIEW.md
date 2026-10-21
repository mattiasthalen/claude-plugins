---
tiers:
  low:
    - "README.md"
    - "docs/**"
  medium:
    - "plugins/**"
    - "evals/**"
    - "evals/**/graders/**"
    - "scripts/**"
  high:
    - "REVIEW.md"
    - ".github/**"
    - ".claude/**"
    - "**/hooks/**"
    - ".claude-plugin/marketplace.json"
    - "plugins/*/.claude-plugin/plugin.json"
---

# Review

What matters when reviewing a change to this marketplace. `sdlc`'s review stage reads this file; the tiers above set how deep review goes and whether the evidence gate stops ([ADR-0011](docs/decisions/0011-risk-tiers-are-set-by-changed-paths-in-review-md-frontmatter.md)). A path takes the highest tier any of its globs matches, and a change the highest tier of its paths: a plugin README is Medium, since `plugins/**` matches it.

## What failure looks like

A plugin here fails in one of three ways. Look for these first:

- **It misfires.** A skill triggers on a conversation it should not, or stays silent on one it exists for. Check every description change against the cases in `evals/<plugin>/` that grade triggering.
- **It misroutes.** A stage hands off to the wrong next stage, skips a gate, resumes at the wrong place, or invokes the wrong skill. Check the order the skill states against the order its cases grade.
- **It lies.** A skill or document claims what is not so: a check reported green that was not run, a README describing behaviour the skill does not have, an ADR whose Decision the code contradicts. Quote both sides.

A skill line with no case that fails without it is a finding ([ADR-0012](docs/decisions/0012-the-eval-gate-runs-in-session-and-stage-lines-start-empty.md)).

## Nits

At most three per review, and only after every defect. A nit in code the change did not touch is `Pre-existing` and goes to follow-ups.

## Skip

- `plugins/*/skills/pr/` except `VENDORED.md`: a vendored copy, changed only by `scripts/vendor.sh`.
- `evals/**/history.jsonl`: generated from `conversation.md` by `evals/sdlc/tools/rebuild_histories.py`.
- `evals/**/results/`.

## Evidence

Every finding cites `file:line` and quotes the line. A finding inferred from a file or function name, without reading it, is not a finding.

## Summary

Start with the count: "3 findings: 1 defect, 2 nits." When there is nothing to fix, say "0 findings" and stop.

## plugins/**/skills/**

A skill is a prompt. Read it as the agent will: a step without a completion criterion, a prohibition where a positive instruction would do, a line restating the default — each is a defect in the skill, not a style point. The `writing-for-agents` skill is the reference.

## evals/**

A grader that passes on a wrong run, or fails on a right one, is the worst defect here: lines are earned against it. Every regex grader has must-pass and must-fail samples in its scenario's `grader-samples.md`.

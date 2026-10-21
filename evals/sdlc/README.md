# sdlc eval suite

What `sdlc` must do, stage by stage. Its lines are earned against this suite ([ADR-0012](../../docs/decisions/0012-the-eval-gate-runs-in-session-and-stage-lines-start-empty.md)): a stage file starts empty and a line enters only when a case fails without it. Every case grades sequence — which stage ran, what it read, where it stopped — not only output. The interview itself is the exodus plugin's business and is not graded here.

## Run

```sh
evals/fetch-deps.sh
python3 evals/sdlc/tools/rebuild_histories.py
claude plugin eval . --eval-dir evals/sdlc --model claude-opus-5-5 --judge-model claude-opus-5-5 \
  --ablation none --scaffold --allow-tools Write Edit Bash -j 4 --trust-plugin \
  --json evals/results/sdlc.json
python3 evals/sdlc/tools/report.py evals/results/sdlc.json
```

One case: `--case 's1-build' --runs 1`. Rerun the [runner probes](../probes/README.md) after a Claude Code upgrade: what they find (no plan mode, no Artifact tool, only Homebrew's `git`, worktrees only with `--no-checkout`, unauthenticated `gh`) shapes what these cases can grade.

## Bars

Each case's `prompt.md` sets its `runs:` by its tier ([ADR-0012](../../docs/decisions/0012-the-eval-gate-runs-in-session-and-stage-lines-start-empty.md)): High (8) must pass every run; Medium (3) passes its `shape-*` graders 3 of 3 and its `content-*` (judged) graders 2 of 3; Low (1) passes once. A global `--runs` overrides them, so pass it only while iterating. A grader that cannot hold its bar on an unchanged skill is fixed or deleted.

## Layout

```
<sN-scenario>/
  scenario.md          what the scenario plants and what a good run does
  grader-samples.md    must-pass / must-fail samples for its regex shape graders
  <stage>/
    case.yaml          scaffold and, for resumed stages, the history
    prompt.md          the requester's next turn, run settings in frontmatter
    scaffold.sh        calls lib/scaffold.sh with the fixtures to copy
    conversation.md    the conversation so far (resumed stages)
    history.jsonl      built from conversation.md
    graders/
fixtures/              the repos cases run in; scaffolding fixes commit dates so SHAs quoted in histories hold
lib/scaffold.sh
tools/                 compose_history.py, rebuild_histories.py, test_shape_graders.py, report.py
```

**Before a run, and after every edit to the skill, run `python3 evals/sdlc/tools/rebuild_histories.py`**: a history embeds the skill's body and its real base directory where its conversation invokes `/sdlc`, so it is built on each machine and never committed. `python3 evals/sdlc/tools/test_shape_graders.py` checks every regex grader against its samples, offline.

Fixtures and tooling are adapted from [pitch-and-deliver](https://github.com/mattiasthalen/pitch-and-deliver)'s suite.

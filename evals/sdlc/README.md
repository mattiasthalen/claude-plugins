# sdlc eval suite

What `sdlc` must do, stage by stage. Its lines are earned against this suite ([ADR-0012](../../docs/decisions/0012-the-eval-gate-runs-in-session-and-stage-lines-start-empty.md)): a stage file starts empty and a line enters only when a case fails without it. Every case grades sequence — which stage ran, what it read, where it stopped — not only output. The interview itself is the exodus plugin's business and is not graded here.

## Run

```sh
evals/fetch-deps.sh
claude plugin eval . --eval-dir evals/sdlc --model claude-opus-5-5 --judge-model claude-opus-5-5 \
  --ablation none --scaffold --allow-tools Write Edit Bash --runs 5 -j 4 --trust-plugin \
  --json evals/results/sdlc.json
python3 evals/sdlc/tools/report.py evals/results/sdlc.json
```

One case: `--case 's1-build' --runs 1`. Rerun the [runner probes](../probes/README.md) after a Claude Code upgrade: what they find (no plan mode, no Artifact tool, only Homebrew's `git`, worktrees only with `--no-checkout`, unauthenticated `gh`) shapes what these cases can grade.

## Bars

`shape-*` graders are deterministic and must pass 5 of 5 runs; `content-*` graders are judged and must pass 4 of 5. An intermittent result is rerun at 8 runs before it is trusted. A grader that cannot hold its bar on an unchanged skill is fixed or deleted.

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
tools/                 compose_history.py, rebuild_histories.py, test_shape_graders.py, report.py, ablate.py, test_ablate.py
```

**After every edit to the skill, run `python3 evals/sdlc/tools/rebuild_histories.py`**: a history embeds the skill's body where its conversation invokes `/sdlc`. `python3 evals/sdlc/tools/test_shape_graders.py` checks every regex grader against its samples, offline.

Fixtures and tooling are adapted from [pitch-and-deliver](https://github.com/mattiasthalen/pitch-and-deliver)'s suite.

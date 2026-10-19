# delivery eval suite

What `delivering-pitches` must do, stage by stage. Its lines are earned against this suite ([ADR-0004](../../docs/decisions/0004-skill-lines-are-earned-by-evals-and-ablation.md)): a line enters only when a case fails without it, and stays only if deleting it drops a grader below its bar. The interview and review themselves are the exodus plugins' business and are not graded here.

## Run

```sh
evals/fetch-deps.sh
claude plugin eval . --eval-dir evals/delivery --model claude-opus-5-5 --judge-model claude-opus-5-5 \
  --ablation none --scaffold --allow-tools Write Edit Bash --runs 5 -j 4 --trust-plugin \
  --json evals/results/delivery.json
python3 evals/delivery/tools/report.py evals/results/delivery.json
```

One case: `--case 's1-build' --runs 1`. Rerun the [runner probes](../probes/README.md) after a Claude Code upgrade: what they find (no plan mode, no Artifact tool, no `git`, unauthenticated `gh`) shapes what these cases can grade.

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
tools/                 compose_history.py, rebuild_histories.py, test_shape_graders.py, report.py, ablate.py
```

**After every edit to the skill, run `python3 evals/delivery/tools/rebuild_histories.py`**: a history embeds the skill's body where its conversation invokes `/delivery:delivering-pitches`. `python3 evals/delivery/tools/test_shape_graders.py` checks every regex grader against its samples, offline.

Fixtures and tooling are adapted from [pitch-and-deliver](https://github.com/mattiasthalen/pitch-and-deliver)'s suite.

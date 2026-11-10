# Evals

Suites for this marketplace's own plugins, run with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Cases test our plugins only; upstream plugins load as dependencies and their behaviour is left to their own suites.

## Run

In a Linux cloud container, first: `apt-get update && apt-get install -y bubblewrap socat`.

```sh
evals/fetch-deps.sh          # design, implementation, mattpocock-skills at their default branch; prints their versions
python3 evals/sdlc/gen.py    # writes evals/sdlc/cases/ (git-ignored); re-run after any SKILL.md change
claude plugin eval . --eval-dir evals/sdlc --ablation none --trust-plugin --scaffold \
  --allow-tools Write Edit Bash --model claude-opus-5-5 --judge-model claude-opus-5-5 -j 8
```

Upstream's head can be ahead of the version an install runs (ADR-0002); compare the versions `fetch-deps.sh` prints with `claude plugin list`.

One case: `--case <name>`. Several `--case` flags don't combine; run one per case. `--keep-temp` keeps each run's trace for reading.

Bars: 3 runs per case; shape graders pass 3 of 3, judges 2 of 3. Read a run's `error` before trusting its score: a `not_contains` grader passes on a run that never acted.

## Earning a line

A skill line is earned when its case is red without it and green with it. To show the red half, copy the plugin, take the line out, and point the suite at the copy:

```sh
cp -R plugins/sdlc .eval-deps/ablate && $EDITOR .eval-deps/ablate/skills/<skill>/SKILL.md
SDLC_PLUGIN=.eval-deps/ablate python3 evals/sdlc/gen.py   # then run the line's case as above
```

Stop as soon as the red half is decided. Only a run with no `error` that did not time out counts; rerun any other. A shape grader's bar is 3 of 3, so one failed run misses it: run the line's case with `--runs 1`, and a failure of the line's own shape grader earns the line; only a pass goes on to three runs. When the line's grader is a judge, its bar is 2 of 3 and one failure is not enough: start with `--runs 2`, where two failures earn the line, two passes mean it is not earned, and a split takes one more run. The green half, with the line in, always runs three.

## The sdlc suite

`gen.py` holds every case: each starts at one step of the flow on the ordersdesk fixture (`lib/scaffold.sh` builds its states), with the conversation so far as a seeded history and the requester's next line as the prompt. The eval runner names no scratchpad, so each case names `.scratchpad/` in the workspace, which the fixture's git ignores.

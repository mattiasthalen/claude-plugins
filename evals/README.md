# Evals

Suites for this marketplace's own plugins, run with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Cases test our plugins only; upstream plugins load as dependencies and their behaviour is left to their own suites.

## Run

In a Linux cloud container, first: `apt-get update && apt-get install -y bubblewrap socat`.

```sh
evals/fetch-deps.sh          # design, implementation, mattpocock-skills at their default branch
python3 evals/sdlc/gen.py    # writes evals/sdlc/cases/ (git-ignored); re-run after any SKILL.md change
claude plugin eval . --eval-dir evals/sdlc --ablation none --trust-plugin --scaffold \
  --allow-tools Write Edit Bash --model claude-opus-5-5 --judge-model claude-opus-5-5 -j 8
```

One case: `--case <name>`. Several `--case` flags don't combine; run one per case. `--keep-temp` keeps each run's trace for reading.

Bars: 3 runs per case; shape graders pass 3 of 3, judges 2 of 3. Read a run's `error` before trusting its score: a `not_contains` grader passes on a run that never acted.

## Earning a line

A skill line is earned when its case is red without it and green with it. To show the red half, copy the plugin, take the line out, and point the suite at the copy:

```sh
cp -R plugins/sdlc .eval-deps/ablate && $EDITOR .eval-deps/ablate/skills/<skill>/SKILL.md
SDLC_PLUGIN=.eval-deps/ablate python3 evals/sdlc/gen.py   # then run the line's case as above
```

## The sdlc suite

`gen.py` holds every case: each starts at one step of the flow on the ordersdesk fixture (`lib/scaffold.sh` builds its states), with the conversation so far as a seeded history and the requester's next line as the prompt. The eval runner names no scratchpad, so each case names `.scratchpad/` in the workspace, which the fixture's git ignores.

# Evals

Eval suites for this marketplace's own plugins, run with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). They live at the repo root, outside `plugins/`, so they never ship with a plugin. Layout follows [the-exodus/claude-design-skills](https://github.com/the-exodus/claude-design-skills/tree/main/evals): one directory per case, a `prompt.md` and `graders/*.md`, each case naming the plugins it loads in `plugins:`.

Cases test our plugins only. A plugin pulled in from elsewhere (`design`) is loaded as a dependency and its own behaviour is left to its own suite.

## Run

```sh
evals/fetch-deps.sh
claude plugin eval . --model claude-opus-5-5 --judge-model claude-opus-5-5 --ablation none --allow-tools EnterPlanMode
```

`fetch-deps.sh` sparse-checks-out `design` into `.eval-deps/` (gitignored), from upstream main as the marketplace resolves it; only the plugin directory, so the runner never picks up the upstream repo's own cases. Re-run it to pick up a new upstream version.

`--ablation none`: the cases invoke a user-invoked skill by name, so a no-plugin arm scores 0 by construction. One case cheaply: `--case <name> --runs 1`. Results land in `evals/results/`, gitignored.

## Cases

| Case | Checks |
|---|---|
| `design-and-build/starts-with-plan-mode-interview` | invoked with a pitch, the skill enters plan mode before loading `design:design-interview`, by its qualified name, and does not present a plan on the first turn |

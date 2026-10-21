# sdlc

An AI-native software development life cycle, after Anthropic's [AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) and [how they solved code review](https://claude.dev/blog/solving-code-review-at-anthropic/). `/sdlc <intent>` takes one change from an intent (a ticket, free text, a file) to ready pull requests. You approve four documents on the way; between the last two it runs on its own.

```
/plugin install sdlc@mattiasthalen
```

Installing it also installs Tobias Karlsson's [claude-design-skills](https://github.com/the-exodus/claude-design-skills) `design` and `implementation`, pinned to a commit in this marketplace. `sdlc` uses their interview, decision records, lexicon, design philosophy and code style.

## Stages

| Stage | Writes | Ends at |
|---|---|---|
| spec | `spec.md`: acceptance criteria (some of them preservation criteria: "this must not change"), edge cases, each with a check and its design branch | **gate**: approve the spec |
| plan | `plan.md`: slices, order, what each check verifies | **gate**: approve the plan |
| test | the tests, written by the `test-writer` agent from the spec alone, run at the base | **gate**: approve the tests (change criteria red, preservation criteria green) |
| build | the change | — unattended — |
| review | fixes: parallel reviewers by lens, at Medium and High three verifiers voting on each finding, a blocking security pass, at most three rounds | — unattended — |
| prove | `evidence.md`: each check at the head, plus CI and the existing suite | **gate**: approve the evidence (Low-risk changes skip it) |
| ship | ready pull requests with a conventional body: Summary, Testing, Risk, How to revert | |

Every gate, and every early stop, asks whether to continue here, continue in a new session (and where to keep the documents), or stop. `/sdlc continue from <stage> using <paths>` resumes a run. The documents live in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-<session>/` without one; nothing is committed but the change itself.

## Risk

A repository's `REVIEW.md` frontmatter maps paths to `low`, `medium` and `high`; the highest one a change touches sets its tier. Without it, everything is Medium. `REVIEW.md`, CI and hook configuration are always High. Low opens its pull request on green without stopping for you; High asks you to read the diff, not only the evidence.

## The stage hook

While a run is going, a hook refuses file writes the stage should not make: nothing outside the run's documents before the plan is approved, only tests during the test stage, and no test edits after it except by the `test-writer`. It does nothing outside a run.

## Progress

The run keeps a task list. In the CLI, task tools are off by default on current models; turn them on with `{ "env": { "CLAUDE_CODE_ENABLE_TODO_TOOLS": "1" } }` in `~/.claude/settings.json`.

## Credits

The pull request body starts from Matt Pocock's [`pr`](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill, vendored in `skills/pr/` (MIT; see its `VENDORED.md`). The interview, records, style and review lenses are Tobias Karlsson's.

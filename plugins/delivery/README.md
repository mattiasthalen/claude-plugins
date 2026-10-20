# delivery

Anything in, a pull request out. `/delivery:delivering-pitches <pitch>` takes one feature from a pitch (prose, a ticket or issue link, a path) through a design interview, a plan, the build, review and an evidence gate, to ready pull requests.

```
/plugin install delivery@mattiasthalen
```

Installing it also installs its two dependencies from this marketplace, Tobias Karlsson's [claude-design-skills](https://github.com/the-exodus/claude-design-skills): `design` (the interview, ADRs, lexicon) and `implementation` (code style, the review cycle). `delivery` sequences them and owns only what they leave out: the plan's shape with guardrails, slicing, the evidence gate and pull requests.

## What a run looks like

1. **Interview**, in plan mode where it exists: `design:design-interview` through its wrap-up. Say the change is small and it is skipped; the plan and its brief never are.
2. **Plan**: the design tree, then a brief whose every criterion, edge case and guardrail has a check and the branch it came from, then slices, the records to write, and progress. A fresh subagent checks it before you see it.
3. **Build**, after you approve: the records first, then each slice.
4. **Review** with `implementation:review-cycle`.
5. **Evidence**: every check run at the base and at the head, each guardrail against a mutant, published as a page. Approve it, or ask for a change.
6. **Pull requests**, ready for review, one per slice and repo.

## Progress

The run keeps a task list. The Claude desktop app shows its own; in the CLI, task tools are off by default on current models, so turn them on:

```json
{ "env": { "CLAUDE_CODE_ENABLE_TODO_TOOLS": "1" } }
```

in `~/.claude/settings.json`.

## Credits

The pull request body is Matt Pocock's [`pr`](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill, vendored in `skills/pr/` (MIT; see its `VENDORED.md`), which in turn credits humanlayer's `show-me`. The interview, records, style and review are Tobias Karlsson's. The evidence gate and eval approach come from [pitch-and-deliver](https://github.com/mattiasthalen/pitch-and-deliver).

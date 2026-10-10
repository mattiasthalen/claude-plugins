# design-and-build

`/design-and-build:design-and-build <pitch>` runs a design interview in plan mode, gap-checks it, doubts the brief, gets a plan carrying the brief approved, then captures ADRs, builds test-first through a subagent, reviews with an adversarial pass each round and opens a draft PR.

Depends on, both listed in this marketplace and installed alongside:

- `design` (Tobias Karlsson's [claude-design-skills](https://github.com/the-exodus/claude-design-skills)): the interview, philosophy, ADR and lexicon skills.
- `agent-skills` (Addy Osmani's [agent-skills](https://github.com/addyosmani/agent-skills), MIT): the builder's `test-driven-development` and `incremental-implementation`. The run halts at the build step without them.

The doubt pass prompt is adapted from agent-skills' `doubt-driven-development` (MIT, © Addy Osmani).

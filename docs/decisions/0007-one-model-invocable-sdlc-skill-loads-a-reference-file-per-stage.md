# ADR-0007 — One model-invocable sdlc skill loads a reference file per stage

**Status:** Accepted (2026-10-21); partly superseded by [ADR-0015](0015-every-fresh-sdlc-run-starts-with-an-intent-stage-that-writes-user-stories.md) (stage list, 2026-10-23) · **Supersedes:** [ADR-0001](0001-delivery-delegates-design-style-and-review-to-the-exodus-skills.md)

## Context

ADR-0001 kept `delivery` as one user-invoked skill that delegated design, style and review to Tobias Karlsson's `design` and `implementation` plugins on their default branch, and rejected a split into per-stage skills because Claude Code blocks Claude from invoking a skill with `disable-model-invocation`. `delivery` is being replaced by `sdlc`, shaped on Anthropic's AI-native SDLC playbook: spec, plan, test, build, review, prove and ship, each reading the previous stage's documents. Dogfooding `delivery` showed the cost of a user-only entry: a session started from another session could not invoke it and waited until the requester typed the command. `sdlc` now owns the review stage itself (ADR-0010).

## Decision

`sdlc` is one model-invocable skill, `plugins/sdlc/skills/sdlc/`, whose description fires only on a request to run the SDLC on an intent or to continue from a named stage with document paths. It owns the stage order, the seams between stages and resumption. Each stage is a reference file under `references/` (`spec`, `plan`, `test`, `build`, `review`, `prove`, `ship`), loaded when its stage starts. `design` and `implementation` stay dependencies, pinned by `sha` in the marketplace, for the interview, records, philosophy and code style only.

Rejected:
- Model-invocable per-stage skills: each description is a trigger surface on unrelated conversations and needs its own negative trigger case.
- A user-only `/sdlc`: a session started from another session cannot resume a stage on its own.
- Vendoring all of `claude-design-skills`: it carries no licence, so a copy is not ours to redistribute.

## Consequences

- A chip resumes with "continue from <stage> using <paths>" and no keystroke from the requester.
- A negative trigger case guards the one description.
- Per-stage entry points do not exist until use earns them; promoting a reference file to a skill is cheap.
- Upstream pins move only by a deliberate bump.

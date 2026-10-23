# ADR-0009 — Tests are written and approved before the build, and only by the test writer

**Status:** Accepted (2026-10-21) · **Supersedes:** [ADR-0002](0002-evidence-baseline-is-recomputed-by-overlaying-checks-on-the-base.md)

## Context

ADR-0002 had `delivery` write each check after plan approval, alongside the build, and recompute the evidence at the end by overlaying HEAD's checks on a copy of the base, with a mutant per guardrail. `delivery` approved its plan in plan mode, whose read-only harness also blocked side notes and dictated how each turn ended. The playbook commits a failing test first and blocks test edits during the fix. Discussion with Tobias Karlsson settled that "must not change" is an acceptance criterion like any other, and that a change can only be shown to do what was asked while the existing suite passes: no check proves nothing broke. An agent works best with every test written up front, since passing tests are how it knows it is done.

## Decision

`sdlc` uses no plan mode. Its gates are the seams after the spec, the plan, the tests and the evidence; the requester reviews each document in the desktop file pane and approves in chat. After plan approval, a test stage runs the `test-writer` agent, which writes, moves or deletes every test and judged rubric from the spec and the plan's check descriptions alone, and runs them at the base. The test gate shows each base result: a change criterion red, a preservation criterion green; anything else is flagged. From the build on, only the `test-writer` may write tests, including a regression test a review finding proves missing, which becomes a new criterion. A plugin hook enforces the phases: before plan approval, writes go only to the scratchpad; in the test stage, only to test files; afterwards, never to test files outside the `test-writer`. The prove stage also asserts that no test file changed after the test gate outside its commits. Build, review and prove then run unattended; evidence is each criterion's check at HEAD plus the repository's CI and existing suite, and anything red there means no pull request.

Rejected:
- Plan mode: the harness forces the shape of every turn and blocks writing outside the plan file.
- Writing checks in the plan stage: approving the plan would mix the how with the oracle.
- Mutants and a base overlay at the end: the base is already shown at the test gate, and a surviving mutant proves only the one thing it mutates.

## Consequences

- The builder can never shape its own oracle; a wrong check routes back to a re-plan.
- The run is unattended between the test gate and the evidence gate, so permission prompts stall it unless auto mode or allowed tools cover the build.
- The hook needs run state keyed per session so parallel runs do not share a phase.

## Addendum 2026-10-23

[ADR-0015](0015-every-fresh-sdlc-run-starts-with-an-intent-stage-that-writes-user-stories.md) adds the intent gate before the spec gate. It is a gate like the others: it shows `intent.md` whole, always stops, and is a seam (continue here, in a new session from `intent.md`'s path, or stop). The hook treats `intent` as a pre-approval phase, like `spec` and `plan`: writes go only into the run's folder.

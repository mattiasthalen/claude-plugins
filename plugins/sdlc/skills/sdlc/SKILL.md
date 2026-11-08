---
name: sdlc
description: Runs one change through the SDLC — spec, plan, tests, build, review, evidence, pull requests — from an intent (a ticket, text or file), or continues a run from a named stage given its documents' paths.
argument-hint: "<intent> | continue from <stage> using <paths>"
---

An intent, from user stories to ready pull requests, in eight stages: intent once, then spec to ship for each delivery. Each stage is its own skill, holding that stage's rules; this one only starts the run and hands it to the right stage.

| Stage | Skill | Writes | Ends at |
|---|---|---|---|
| intent | `sdlc:intent` | `intent.md` | the intent gate |
| spec | `sdlc:spec` | `spec.md`, and the design interview's `capture/` and `brief/` | the spec gate |
| plan | `sdlc:plan` | `plan.md` | the plan gate |
| test | `sdlc:test` | the tests | the test gate |
| build | `sdlc:build` | the change | review, unattended |
| review | `sdlc:review` | fixes | prove, unattended |
| prove | `sdlc:prove` | `evidence.md` | the evidence gate |
| ship | `sdlc:ship` | pull requests | done |

**Start.** Keep the stages as a task list from this first turn, spec to ship once per delivery. Then invoke the stage's skill with the Skill tool before doing anything else, and follow it:

- a new intent starts at `sdlc:intent`;
- "continue from <stage> using <paths>" starts at that stage's skill with those documents, which must exist and be read first; a missing one is refused with its path and the run asks for it.

Every stage ends by invoking the next one's skill; never run a stage from memory of its rules.

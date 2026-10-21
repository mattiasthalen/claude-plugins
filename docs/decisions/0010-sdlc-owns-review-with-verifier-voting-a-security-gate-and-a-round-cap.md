# ADR-0010 — sdlc owns review, with verifier voting, a security gate and a round cap

**Status:** Accepted (2026-10-21)

## Context

`delivery` ran `implementation:review-cycle`, which briefs fresh-context reviewers by lens, then lets the authoring session triage, fixes each defect test-first, and records dispositions on a tracker. Anthropic's code-review flow adds independent verification (a separate group votes on each finding), a security pass that blocks merge, a `Pre-existing` tag (59% of repeated flags in one 50-round loop were first-pass code), a ledger that never repeats a finding, diff-only re-review and a cap of three rounds. `review-cycle` is Tobias Karlsson's, releases often, and its test-first fix and tracker comment conflict with ADR-0009 and ADR-0008. This repository has no Claude GitHub app; review runs in the session before the pull request opens.

## Decision

`sdlc`'s review stage is its own. Finders run in parallel by lens, using `review-cycle`'s lens briefs by reference and the repository's `REVIEW.md`. At Medium and High risk, three fresh verifiers vote on each finding and a majority keeps it; the authoring session fixes and never triages. A security pass runs at every tier (`/security-review`, or a security-lens subagent where it is absent), and no evidence gate is reached while a bug or security finding is open: each is fixed or closed with a reason shown in the evidence. A per-repository ledger in the scratchpad tags findings whose code predates the change as `Pre-existing` (by `git blame` against the base) and sends them to follow-ups, never repeats a finding, re-reviews only the diff after the first round, sweeps for the finding's class, and stops after three rounds.

Rejected:
- Wrapping `review-cycle` and overriding its fix and record steps: brittle against an upstream that changes weekly.
- Proposing the additions upstream and waiting: the requester's choice.

## Consequences

- Review costs more agent runs per finding; tuning voting is left until the cost bites.
- Finding dispositions are not kept past the run; reviewer evals come from what escaped, not from per-run outcomes.
- A lens brief renamed upstream breaks the reference until the pin is bumped.

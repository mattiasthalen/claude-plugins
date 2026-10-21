# ADR-0011 — Risk tiers are set by changed paths in REVIEW.md frontmatter

**Status:** Accepted (2026-10-21)

## Context

Anthropic sets a change's risk from the change, not its author, and lets low-risk changes merge on automated checks alone. Their `REVIEW.md`, written by code owners, says what matters in a repository. This repository has one maintainer, so tiers cannot drive the number of approvers; GitHub cannot require a self-approval and an agent's approval never counts.

## Decision

A repository's root `REVIEW.md` carries YAML frontmatter mapping path globs to `low`, `medium` and `high`, and prose for reviewers: what failure looks like, a nit cap, paths to skip, `file:line` evidence, a count-first summary, and `## <glob>` lens sections. A change takes the highest tier any changed path matches; unmatched paths, and repositories without `REVIEW.md`, are Medium. `REVIEW.md` itself, CI configuration and hook or permission configuration are High whatever the file says. Low runs lenses by signal and the security pass, and opens its pull request on green without stopping at the evidence gate. Medium adds verifier voting and stops for the requester. High runs every lens and asks the requester to read the diff. `sdlc` never creates a `REVIEW.md` unasked; for review it wins over `CLAUDE.md`, and a conflict is reported as a finding against `CLAUDE.md`.

Rejected:
- A separate tier file: it splits what matters from how much it matters, and the two drift.
- Tiers driving approver count: one maintainer.

## Consequences

- A change can lower its own scrutiny only through a High-tier edit to `REVIEW.md`.
- CI and the review stage read one source for risk.
- Nested `REVIEW.md` files wait for a second owner.

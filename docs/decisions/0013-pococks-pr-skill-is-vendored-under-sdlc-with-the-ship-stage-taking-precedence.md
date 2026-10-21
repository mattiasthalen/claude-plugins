# ADR-0013 — Pocock's pr skill is vendored under sdlc, with the ship stage taking precedence

**Status:** Accepted (2026-10-21) · **Supersedes:** [ADR-0003](0003-pococks-pr-skill-is-vendored-pinned-with-delivery-taking-precedence.md)

## Context

ADR-0003 copied Matt Pocock's `pr` skill (MIT) unchanged into `plugins/delivery/skills/pr/` at `mattpocock/skills@e484a80`, refreshed by `scripts/vendor-pr.sh`, with `delivering-pitches` winning where they conflict. `delivery` is removed in favour of `sdlc`, and `sdlc`'s pull request body is conventional (ADR-0008).

## Decision

The same copy moves to `plugins/sdlc/skills/pr/`, unchanged and pinned, listed in the manifest that `scripts/vendor.sh` checks and refreshes. A repository hook refuses edits to it from Claude. Where it conflicts with `sdlc`'s ship stage — screenshots, a glossary, its section layout — the ship stage wins: the repository's pull request template, or Summary, Testing, Risk and How to revert, with no images and the project's own lexicon.

Rejected:
- Depending on `mattpocock-skills`: 26 competing skills come with it.
- Dropping `pr` for a template in the ship stage: loses the provenance and refresh path.

## Consequences

- A weekly refresh job opens a draft pull request when the upstream copy moves.
- If Pocock ships `pr` on its own, the copy should become a dependency.

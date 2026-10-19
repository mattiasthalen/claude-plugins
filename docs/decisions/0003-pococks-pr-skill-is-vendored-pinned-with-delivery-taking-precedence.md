# ADR-0003 — Pocock's pr skill is vendored, pinned, with delivery taking precedence

**Status:** Accepted (2026-10-20)

## Context

The pull request body follows Matt Pocock's `pr` skill (MIT): Summary as the smallest view that makes the point, before/after Evidence, Merge Danger. It ships only inside `mattpocock-skills`, one plugin of 27 skills, among them `tdd`, `code-review`, `implement` and `grilling`, which trigger on their own and compete with the exodus skills mid-delivery. A `git-subdir` source cannot select one skill: `skills/engineering/pr` has no `plugin.json`. Pocock himself copies humanlayer's `show-me` into `pr` with a `CREDITS.md` for the same reason.

## Decision

`skills/engineering/pr/` is copied unchanged into `plugins/delivery/skills/pr/`, pinned to `mattpocock/skills@e484a80`, with a `VENDORED.md` naming the source, commit and licence, and `scripts/vendor-pr.sh` to check or refresh it. It stays model-invocable so `delivering-pitches` can invoke `delivery:pr`, then adds a Brief section. Where the vendored text conflicts with `delivering-pitches` — screenshots as evidence, `GLOSSARY.md` — `delivering-pitches` wins: no images, the project's own lexicon.

Rejected:
- Depending on `mattpocock-skills`: 26 competing skills come with it.
- Rewriting the template in `delivering-pitches`: loses the provenance and the refresh path.

## Consequences

- A model-invocable `delivery:pr` can also fire outside a delivery; it only drafts a body.
- Upstream changes to `pr` arrive only through a deliberate refresh.
- If Pocock ships `pr` on its own, the copy should become a dependency.

# ADR-0002 — Upstream plugins follow their default branch, unpinned and uncopied

**Status:** Accepted (2026-11-10)

## Context

`sdlc` depends on three plugins it does not own: Tobias Karlsson's `design` and `implementation` (the-exodus/claude-design-skills) and Matt Pocock's `mattpocock-skills` (mattpocock/skills, a plugin at its repo root). The first `sdlc` pinned design and implementation to a commit in the marketplace and copied Pocock's `pr` skill into itself, with a script and a weekly workflow to detect drift and open refresh PRs.

## Decision

The marketplace lists all three from their own repositories with no `sha`, so each follows its default branch and its own `plugin.json` version. `sdlc` declares them as dependencies, so installing `sdlc` installs the flow's skills. Nothing upstream is copied into this repository.

Rejected:

- **Pinning each to a commit:** every upstream fix waits for a bump here, and the bump machinery (vendor script, drift workflow, refresh PRs) is more to maintain than the flow itself.
- **Copying the upstream skills into `sdlc`:** every upstream fix has to go through our copy, and the copy can be edited by accident.

## Consequences

- An upstream change can break the flow without any change here. The eval suite catches it only when it is run, which is in-session, before a pull request, since CI has no model token.
- The eval runs fetch upstream at its default branch, so two runs on different days can load different upstream skills. A result is only comparable to another taken the same day.
- There is no vendor script, vendor manifest or refresh workflow.

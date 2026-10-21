# ADR-0008 — sdlc keeps spec, plan and evidence in the session scratchpad

**Status:** Accepted (2026-10-21)

## Context

The playbook commits `intent.md`, `spec.md` and `plan.md` to the repo as an audit trail. `sdlc` is the requester's own factory and runs in repositories other developers share; one spec can fan out to several repos and pull requests. The intent arrives in whatever form the requester has: a ticket, free text, a file.

## Decision

The intent is taken as it arrives and written to a file only at a seam that leaves the session. `spec.md`, `plan.md` and `evidence.md` live in the session scratchpad, or under `$TMPDIR` where there is none, and are consumed by later stages. Every seam asks whether to continue here, start the next stage in a new session (and where to write the documents), or stop; a new session gets the documents' absolute paths. Each pull request body is conventional — Summary, Testing (the evidence for its slice's criteria), Risk, How to revert — and carries no spec or design tree.

Rejected:
- Committing the artifacts: clutter in shared repos.
- A draft pull request as the artifacts' home: noise before code exists, several drafts for a multi-repo spec.
- The tracker as home: one adapter per tracker, a re-sync on every amended spec, and outward writes at every gate. Mirroring to tracker sub-tasks is left behind a per-gate publish step until a ticket is worth mirroring.

## Consequences

- Nothing `sdlc`-shaped reaches other developers beyond a conventional pull request.
- A spec outlives the session only where the requester puts it at a seam.
- A later tracker adapter plugs into the publish step without touching the stages.

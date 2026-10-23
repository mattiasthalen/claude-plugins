# ADR-0008 — sdlc keeps spec, plan and evidence in the session scratchpad

**Status:** Accepted (2026-10-21); partly superseded by [ADR-0015](0015-every-fresh-sdlc-run-starts-with-an-intent-stage-that-writes-user-stories.md) (intent taken as it arrives, 2026-10-23)

## Context

The playbook commits `intent.md`, `spec.md` and `plan.md` to the repo as an audit trail. `sdlc` is the requester's own factory and runs in repositories other developers share; one spec can fan out to several repos and pull requests. The intent arrives in whatever form the requester has: a ticket, free text, a file.

## Decision

The intent is taken as it arrives and written to a file only at a seam that leaves the session. `spec.md`, `plan.md` and `evidence.md` live in the session scratchpad, or under `$TMPDIR` where there is none, and are consumed by later stages. Every gate and every early stop asks whether to continue here, start the next stage in a new session (and where to write the documents), or stop; a new session gets the documents' absolute paths. Each pull request body is conventional — Summary, Testing (the evidence for its slice's criteria), Risk, How to revert — and carries no spec or design tree.

Rejected:
- Committing the artifacts: clutter in shared repos.
- A draft pull request as the artifacts' home: noise before code exists, several drafts for a multi-repo spec.
- The tracker as home: one adapter per tracker, a re-sync on every amended spec, and outward writes at every gate. Mirroring to tracker sub-tasks is left behind a per-gate publish step until a ticket is worth mirroring.

## Consequences

- Nothing `sdlc`-shaped reaches other developers beyond a conventional pull request.
- A spec outlives the session only where the requester puts it at a seam.
- A later tracker adapter plugs into the publish step without touching the stages.

## Addendum 2026-10-23

[ADR-0015](0015-every-fresh-sdlc-run-starts-with-an-intent-stage-that-writes-user-stories.md) adds `intent.md` to the run's folder beside `spec.md`, `plan.md` and `evidence.md`: the intent as user stories, with each story's disposition and the deliveries. It is never committed.

The tracker is no longer only behind a publish step. A story is filed when the requester answers "file" at the intent gate, where and as what the requester's words, the ticket's tracker or the project's docs say. After the spec gate's yes, the spec is published only when the requester or the project's docs say so, where and as what they say, linked to its stories; the published body is the spec's content, never a path into the run's folder. When a published spec is amended and approved again, the run offers to update the published item and does so only on a yes. No tracker adapter exists: the plugin names none and uses whatever the project says. Publishing the plan stays deferred.

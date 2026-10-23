# ADR-0015 — Every fresh sdlc run starts with an intent stage that writes user stories

**Status:** Accepted (2026-10-23) · **Supersedes:** the stage-list decision in [ADR-0007](0007-one-model-invocable-sdlc-skill-loads-a-reference-file-per-stage.md); the intent-as-it-arrives decision in [ADR-0008](0008-sdlc-keeps-spec-plan-and-evidence-in-the-session-scratchpad.md)

## Context

ADR-0007 fixed `sdlc`'s stages as spec, plan, test, build, review, prove and ship, and ADR-0008 took the intent as it arrived, writing it to a file only at a seam that leaves the session. Every run then started from a different shape: a ticket, free text, a file, sometimes an epic that the spec stage could only name the parts of and stop. The requester wants every run to start from one familiar format, user stories, and to decide per story what happens to it, including filing it on the project's tracker for later. The plugin is the requester's own factory across projects with different trackers, so it must not depend on any one of them.

## Decision

`intent` is the first stage of every fresh run; `continue from <stage>` starts later and skips it. It drafts the intent as user stories in `intent.md` in the run's folder before asking anything: each story has an id, As a / I want / So that, acceptance criteria and notes, and what the intent leaves open goes in the notes and is asked at the gate. An intent that already is a story stays one story, refined in place; updating its ticket is offered and done only on a yes.

The intent gate is a gate like the others: it always stops, and it is a seam. Per story it asks now, file or drop; "file" is the yes to file it. "Now" stories are grouped into deliveries of one or several stories, and the deliveries run one after another, each from spec; `intent.md` marks each delivery shipped when its pull requests open, spec takes the first not yet shipped, and each later delivery keeps its documents in a subfolder of the run's folder. A delivery whose pull requests do not open ends the run. The spec traces each criterion to its stories and may add criteria of its own. With no story "now" (every story dropped or filed), the run ends at the gate.

Where and as what a story is filed comes from the requester's words, then the tracker of the ticket it came from, then the project's docs (`CLAUDE.md`, memory, config). The tools within reach never choose: when none of these names a tracker, the run asks; when the requester says there is none, it asks what to do with the stories. A failed filing is reported with the story's text and the run goes on.

Rejected:
- Keeping the intent as it arrives (ADR-0008): every run starts from a different format, and an epic stops at spec with nothing written.
- Running the design interview at the intent stage: it is a spec-stage tool for one change; the intent stage drafts first and asks at its gate.
- A default tracker, or choosing one from the tools available: couples the plugin to a tracker and files where the requester did not ask.
- Publishing the plan as well: deferred until tuning the factory needs it.

## Consequences

- Every run has `intent.md`, and an epic becomes stories the requester can file instead of a stop at spec.
- The spec stage keeps its "more than one change, ask which" backstop for a document handed to `continue from spec` without stories.
- The stage hook treats `intent` as a pre-approval phase: writes go only into the run's folder.
- The skill's description is unchanged, so triggering is unchanged; the stage list grows to eight.

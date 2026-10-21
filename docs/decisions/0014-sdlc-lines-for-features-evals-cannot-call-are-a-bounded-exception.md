# ADR-0014 — sdlc lines for features evals cannot call are a bounded exception

**Status:** Accepted (2026-10-21) · **Supersedes:** [ADR-0006](0006-lines-for-features-evals-cannot-observe-or-call-are-a-bounded-exception.md)

## Context

ADR-0006 let a line use a feature without a failing eval when a probe shows it absent in eval runs, or it is not a Claude Code tool an eval run could call, the line changes how and not what, and it falls back to graded behaviour. It named plan mode, Artifact publishing and the host's task-list tool. `sdlc` drops plan mode (ADR-0009), keeps the other two, and adds an inline widget for the interview's options and a new-session handoff at seams, neither callable in eval runs.

## Decision

The rule stands unchanged. Three `sdlc` lines use it:

- Artifact publishing of `evidence.md`, falling back to the file and a summary in the reply;
- the host task-list tool holding the stages, with per-criterion tasks on TaskCreate (or TodoWrite);
- starting the next stage in a new session, falling back to naming the documents' absolute paths in the reply.

Two lines the design called for are not in the skill yet, because no case fails without them: the inline widget for labelled interview options, and a `## Progress` checklist where there is no task tool. Each enters with a case that grades its fallback.

A line lapses into the ordinary rule when a probe finds its feature present.

Rejected:
- Keeping plan mode as an exception line: `sdlc` no longer uses it.

## Consequences

- What the suite grades for these lines is the fallback.
- Probes are rerun after Claude Code upgrades.

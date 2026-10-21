# ADR-0014 — sdlc lines for features evals cannot call are a bounded exception

**Status:** Accepted (2026-10-21) · **Supersedes:** [ADR-0006](0006-lines-for-features-evals-cannot-observe-or-call-are-a-bounded-exception.md)

## Context

ADR-0006 let a line use a feature without a failing eval when a probe shows it absent in eval runs, or it is not a Claude Code tool an eval run could call, the line changes how and not what, and it falls back to graded behaviour. It named plan mode, Artifact publishing and the host's task-list tool. `sdlc` drops plan mode (ADR-0009), keeps the other two, and adds an inline widget for the interview's options and a new-session handoff at seams, neither callable in eval runs.

## Decision

The rule stands unchanged. Four `sdlc` lines use it:

- Artifact publishing of `evidence.md`, falling back to the file and a summary in the reply;
- the host task-list tool holding the stages only, with per-criterion tasks on TaskCreate (or TodoWrite) and a `## Progress` checklist in `plan.md` where there is no task tool;
- the inline widget for labelled options on forks a picture explains, falling back to labelled prose options;
- starting the next stage in a new session, falling back to naming the documents' absolute paths in the reply.

A line lapses into the ordinary rule when a probe finds its feature present.

Rejected:
- Keeping plan mode as an exception line: `sdlc` no longer uses it.

## Consequences

- What the suite grades for these lines is the fallback.
- Probes are rerun after Claude Code upgrades.

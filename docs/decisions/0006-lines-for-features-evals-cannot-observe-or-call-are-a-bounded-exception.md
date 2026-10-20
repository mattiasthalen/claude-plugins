# ADR-0006 — Lines for features evals cannot observe or call are a bounded exception

**Status:** Accepted (2026-10-20) · **Supersedes:** [ADR-0005](0005-lines-for-features-evals-cannot-observe-are-a-bounded-exception.md)

## Context

ADR-0005 let a line use a feature eval runs cannot observe, without a failing eval, when a committed probe showed the feature absent. It named three such lines: plan mode, Artifact publishing, and the host's task-list tool. The host tool turned out to fall outside that rule. It is the app's own tool (the desktop app's, which takes a plan of at most twelve steps), not a Claude Code tool, so no eval run can call it and no probe can show it present or absent. Review also found that a twelve-step cap cannot hold one task per criterion, so the task list was split.

## Decision

A line may use a feature without a failing eval when three things hold: a committed probe shows the feature is absent in eval runs, or the feature is not a Claude Code tool an eval run could call; the line changes how something is delivered, not what; and where the feature is absent the line falls back to behaviour the suite grades. Three lines use it:

- plan mode, falling back to the plan in the reply with no writes outside the plan file before approval;
- Artifact publishing, falling back to `.delivering-pitches/evidence.html`;
- the host task-list tool, holding the stages only. Per-criterion tasks go on TaskCreate (or TodoWrite) where they exist, and with no task tool at all the plan's Progress checklist is ticked.

A line lapses into the ordinary rule when a probe finds its feature present.

Rejected:
- Keeping ADR-0005's probe-only rule and dropping the host tool: the requester prefers its live list.
- Putting every task on the host tool: its twelve-step cap cannot hold one task per criterion.

## Consequences

- Probes are rerun after Claude Code upgrades; the host-tool line has none, by construction.
- What the suite grades for these stages is the fallback, not the real feature.

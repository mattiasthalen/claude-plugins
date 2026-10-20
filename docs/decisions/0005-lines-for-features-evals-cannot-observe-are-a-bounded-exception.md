# ADR-0005 — Lines for features evals cannot observe are a bounded exception

**Status:** Accepted (2026-10-20)

## Context

Under ADR-0004 a line enters only when an eval fails without it. Some features `delivering-pitches` must use are absent in `claude plugin eval` runs: plan mode (EnterPlanMode, ExitPlanMode), the Artifact tool, and a host's own task-list tool such as the desktop app's. A line using them can never fail an eval, so it could never be earned.

## Decision

A line may use such a feature without a failing eval when all three hold: a committed probe shows the feature is absent in eval runs; the line changes how something is delivered, not what; and where the feature is absent the line falls back to behaviour the suite grades. Three lines use it: plan mode (fallback: the plan in the reply, no writes outside the plan file before approval), Artifact publishing (fallback: `.delivering-pitches/evidence.html`), and the host task-list tool (fallback: TaskCreate, else the plan's Progress checklist). A line lapses into the ordinary rule when its probe finds the feature present.

Rejected:
- Leaving those lines ungraded and unbounded: nothing would stop the exception growing.
- Dropping the features: plan mode and published pages are what the requester asked for.

## Consequences

- Probes are rerun after Claude Code upgrades.
- What the suite grades for these stages is the fallback, not the real feature.

## Addendum 2026-10-20

The host task-list line has no committed probe of its own. The host tool, such as the desktop app's, is not a Claude Code tool, so nothing an eval run could call would show it present or absent. Its exception rests on that, not on a probe. The skill keeps only the stages on the host tool, which caps a plan at twelve steps, and puts per-criterion tasks on TaskCreate (or TodoWrite) where those exist. With no task tool at all, it ticks the plan's Progress checklist.

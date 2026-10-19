# ADR-0002 — The evidence baseline is recomputed by overlaying HEAD's checks on the base

**Status:** Accepted (2026-10-20)

## Context

The gate shows, per acceptance criterion, a check that fails before the change and passes after; a check that was never red proves nothing. pitch-and-deliver had the build run each check before writing code and report the red, and its own open doubt was that the reply is graded, so a made-up baseline would pass. Commits are atomic: tests land with the code they test.

## Decision

The proving stage recomputes the baseline itself. It checks out each slice's base in a worktree under `.git/delivering-pitches/`, overlays HEAD's check files, and runs them: criteria must fail there, with the real output shown, and pass at HEAD; guardrails must pass at both. Nothing the build reported is trusted.

Rejected:
- A checks-only first commit per slice, giving an auditable red commit: it breaks atomic commits.
- Trusting the build's reported baseline: unverifiable, and the doubt pitch-and-deliver never closed.

## Consequences

- A check that imports code the slice adds fails at base for the wrong reason; the evidence shows the actual error so the reader can judge it.
- Only executable checks get a computed baseline; judged checks are flagged as judged.
- Worktrees live inside `.git`, so they are never tracked and stay writable in the eval sandbox.

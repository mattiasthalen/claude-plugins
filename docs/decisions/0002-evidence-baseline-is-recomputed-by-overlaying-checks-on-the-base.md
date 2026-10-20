# ADR-0002 — The evidence baseline is recomputed by overlaying HEAD's checks on the base

**Status:** Accepted (2026-10-20)

## Context

The gate shows, per acceptance criterion, a check that fails before the change and passes after; a check that was never red proves nothing. pitch-and-deliver had the build run each check before writing code and report the red, and its own open doubt was that the reply is graded, so a made-up baseline would pass. Commits are atomic: tests land with the code they test.

## Decision

The proving stage recomputes the baseline itself. It checks out each slice's base in a worktree under `$TMPDIR/delivering-pitches/`, overlays HEAD's check files, and runs them: criteria must fail there, with the real output shown, and pass at HEAD; guardrails must pass at both. Nothing the build reported is trusted.

Rejected:
- A checks-only first commit per slice, giving an auditable red commit: it breaks atomic commits.
- Trusting the build's reported baseline: unverifiable, and the doubt pitch-and-deliver never closed.

## Consequences

- A check that imports code the slice adds fails at base for the wrong reason; the evidence shows the actual error so the reader can judge it.
- Only executable checks get a computed baseline; judged checks are flagged as judged.
- Worktrees live under `$TMPDIR`, outside the repository, so they are never tracked; it is the one place outside the workspace an eval run may write, while Claude Code's permission layer refuses writes into `.git/`.

## Addendum 2026-10-20

The decision stands: the base is recomputed from a copy, never trusted from the build. Two details of how it is copied changed once probes and traces were in. In eval runs, `git worktree add` runs its checkout through whatever `git` is first on PATH, which is the broken xcrun shim there. Runs therefore make the copy with `git worktree add --no-checkout` followed by `reset --hard`, or with `git archive`, and the skill names both. The location is now `${TMPDIR:-/tmp}/delivering-pitches/<repo>-<sha>/`, because an unsandboxed shell on Linux may have no `TMPDIR`. Each copy is removed once its checks have run.

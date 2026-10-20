---
description: Probe whether an eval run can add a git worktree with Homebrew's git, which commits fine there. Expected to fail (worktree add calls the xcrun shim); delivery's evidence then takes its base copy with git archive (ADR-0002).
max_turns: 8
allowed_tools: [Bash]
---

Run exactly this command once and report its output verbatim: `/opt/homebrew/bin/git worktree add --detach "$TMPDIR/probe-worktree" HEAD && echo "worktree-$((40+4))"`. Do not try to fix any error.

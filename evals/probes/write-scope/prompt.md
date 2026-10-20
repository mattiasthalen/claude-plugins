---
description: Probe where an eval run may write — inside the workspace's .git/ and under $TMPDIR, outside it.
max_turns: 8
allowed_tools: [Bash]
---

Run each command separately and report every output verbatim:
1. `mkdir -p .git/delivering-pitches && echo $((40+2)) > .git/delivering-pitches/probe && echo "inside-git-$(cat .git/delivering-pitches/probe)"`
2. `echo ok > "$TMPDIR/delivery-probe-4471" && echo "tmpdir-$((40+3))"`

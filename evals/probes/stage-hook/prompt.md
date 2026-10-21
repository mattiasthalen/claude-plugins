---
description: Probe that sdlc's stage hook finds the run's folder in an eval sandbox and refuses a repo write before plan approval.
plugins: ["../../../plugins/sdlc", "../../../.eval-deps/claude-design-skills/plugins/design", "../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 20
timeout_seconds: 600
runs: 3
allowed_tools: [Bash, Write, Edit, Read, Skill]
---

/sdlc Add a line to README.md saying orders are listed oldest first.

This is a probe of the plugin's stage hook, not a real change. Do only this: write the spec stage's phase file exactly where the skill says, then run `echo "bash-tmpdir=$TMPDIR"`, then try once to create `probe.txt` in the repository root with the Write tool. Report, verbatim, the phase file's path, the echo's output and what the Write returned, then stop.

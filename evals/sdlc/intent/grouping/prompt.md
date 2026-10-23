---
description: "Intent gate, S1 and S2 together now: intent.md records one delivery of S1+S2 and spec starts once for that delivery."
tags: [intent, gate-intent, stage-spec]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

S1 and S2 together now, as one delivery. S3 drop. Continue here. The `intent.md` shown at the gate is copied to `sdlc-handoff/intent.md` in the workspace; this session's run folder is new, so start from that copy.

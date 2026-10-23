---
description: "Intent gate, S2 file, with neither the requester nor the project naming a tracker: asks where to file S2; no tracker call."
tags: [intent, gate-intent]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

S1 now, S2 file, S3 drop. Continue here. The `intent.md` shown at the gate is copied to `sdlc-handoff/intent.md` in the workspace; this session's run folder is new, so start from that copy.

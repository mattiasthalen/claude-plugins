---
description: "Intent gate, the requester files S2 in Linear while the project's CLAUDE.md names GitHub Issues: the requester wins, no gh issue create."
tags: [intent, gate-intent]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

S1 now, file S2 in Linear, S3 drop. Continue here. The `intent.md` shown at the gate is copied to `sdlc-handoff/intent.md` in the workspace; this session's run folder is new, so start from that copy.

---
description: "Intent gate, both stories filed and none now, on a project whose CLAUDE.md tracks stories as GitHub Issues: filing is attempted with gh issue create, then the run ends with phase done; no spec, no interview."
tags: [intent, gate-intent]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

File both. The `intent.md` shown at the gate is copied to `sdlc-handoff/intent.md` in the workspace; this session's run folder is new, so start from that copy.

---
description: "S1 build, resumed at the approved test gate: build the export without touching tests, review with verifiers and a security pass, prove at head with a test-path diff since the gate, write evidence.md, and stop at the evidence gate (no REVIEW.md: Medium); no PR."
tags: [s1, stage-build]
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 200
timeout_seconds: 3600
runs: 8
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved, continue here: continue from build using sdlc-handoff/spec.md sdlc-handoff/plan.md

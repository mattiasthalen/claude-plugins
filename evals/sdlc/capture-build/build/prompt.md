---
description: "Capture build, resumed at the approved test gate with the spec stage's capture beside the spec and plan: build copies capture/ordersdesk/ to the same paths in the repo and attempts its commit before editing any source, and copies nothing from capture/ledger/."
tags: [capture, stage-build]
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 200
timeout_seconds: 3600
runs: 3
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved, continue here: continue from build using sdlc-handoff/spec.md sdlc-handoff/plan.md

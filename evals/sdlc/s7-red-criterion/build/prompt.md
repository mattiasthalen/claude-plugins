---
description: "S7 build with a criterion that cannot go green (export under 1 µs): an early stop at the evidence gate, red criterion first, continue / re-plan / abandon; never done, no PR."
tags: [s7, stage-build]
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
runs: 8
max_turns: 200
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved, continue here: continue from build using sdlc-handoff/spec.md sdlc-handoff/plan.md

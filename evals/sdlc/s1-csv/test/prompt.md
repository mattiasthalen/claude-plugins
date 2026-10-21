---
description: "S1 test stage, resumed at the approved plan: the test-writer writes the checks, they run at the base, the gate shows each base result and warns the next stretch is unattended; no build."
tags: [s1, stage-test]
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 120
timeout_seconds: 2400
runs: 3
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved, continue here: continue from test using sdlc-handoff/spec.md sdlc-handoff/plan.md

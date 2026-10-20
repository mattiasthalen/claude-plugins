---
description: "S4 build: every criterion green at base; nothing built, no PR."
tags: [s4, stage-build]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 100
timeout_seconds: 1800
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

Approved — go ahead.

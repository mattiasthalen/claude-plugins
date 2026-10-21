---
description: "Negative trigger: a request to talk a design through, with no changes, does not invoke sdlc."
tags: [trigger]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

How would you structure a CSV export in this repo? Just talk it through, no changes.

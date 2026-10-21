---
description: "S9 ship: one PR per slice, slice 2 stacked on slice 1's branch with a merge note in Risk, each body with only its slice's criteria."
tags: [s9, stage-ship]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 80
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved. Open the pull requests.

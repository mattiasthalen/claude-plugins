---
description: "S5 ship: one PR per changed repo, none for docs, merge order api first and the cross-repo criterion in both bodies."
tags: [s5, stage-ship]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 80
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved. Open the pull requests.

---
description: "Ship after evidence approval, but csv-export gained a commit since the approved head: no PR, checks rerun at the new head, approval asked again."
tags: [head-moved, stage-ship, gate-evidence]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 80
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved. Open the pull request.

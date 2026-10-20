---
description: "S1 gate with a conditional yes: a change request, not an approval."
tags: [s1, stage-gate]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 150
timeout_seconds: 2400
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

Looks good, but call the first column `order_id` instead of `id`.

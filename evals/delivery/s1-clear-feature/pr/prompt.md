---
description: "S1 PR stage after approval: delivery:pr, the kept body has the agreed shape, the failed push reported with its fix."
tags: [s1, stage-pr]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

Approved. Open the pull request.

---
description: "S5 PR stage: one PR per changed repo, none for docs, merge order and the cross-repo row in both."
tags: [s5, stage-pr]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 80
timeout_seconds: 1500
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

Approved. Open the pull requests.

---
description: "S3 small change on the requester's say-so: no interview, still a plan with a brief and checks."
tags: [s3, stage-intake]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

/delivery:delivering-pitches Tiny one, no interview needed: `python3 -m orders --version` should print `orders 1.0`.

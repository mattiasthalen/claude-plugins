---
description: "S3 epic: refused as one delivery; parts named; asks which."
tags: [s3, stage-intake]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 30
timeout_seconds: 900
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

/delivery:delivering-pitches Revamp the back office: a CSV export for accounting, a returns flow with refunds, a customer self-service portal, and replace the JSON order store with SQLite.

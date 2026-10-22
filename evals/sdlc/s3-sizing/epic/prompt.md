---
description: "S3 epic through the intent stage: one story per part in intent.md; stops at the intent gate asking dispositions; no design-interview, no spec, no repo writes."
tags: [s3, stage-intent, gate-intent]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc Revamp the back office: a CSV export for accounting, a returns flow with refunds, a customer self-service portal, and replace the JSON order store with SQLite.

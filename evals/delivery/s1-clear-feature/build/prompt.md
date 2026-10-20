---
description: "S1 build from the approved plan: capture, tasks, review-cycle, evidence with base/head and guardrail mutants, the page, no PR before approval."
tags: [s1, stage-build]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 200
timeout_seconds: 3000
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

Approved — go ahead.

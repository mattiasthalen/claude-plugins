---
description: "Invoked with a pitch, design-and-build creates its progress task list, then loads design:design-interview by its qualified name."
tags: [design-and-build, smoke]
plugins: ["../../../plugins/design-and-build", "../../../.eval-deps/claude-design-skills/plugins/design"]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/design-and-build:design-and-build Add per-customer rate limiting to our public REST API, so one noisy customer can't starve the others.

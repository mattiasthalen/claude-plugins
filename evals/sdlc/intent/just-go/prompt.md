---
description: "Intent stage, the requester declines the interview: stories written from the intent alone, unknowns in notes, no spec; still stops at the intent gate."
tags: [intent, stage-intent, gate-intent]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc Make orders easier for the back office to work with. Just go, don't ask me anything.

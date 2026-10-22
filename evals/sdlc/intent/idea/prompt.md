---
description: "Intent stage, fresh and vague: intent.md with user stories in the run folder, phase intent, no spec, no design-interview, no repo writes; stops at the intent gate asking dispositions and the seam."
tags: [intent, stage-intent, gate-intent]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc Make orders easier for the back office to work with.

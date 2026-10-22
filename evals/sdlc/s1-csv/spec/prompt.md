---
description: "S1 spec stage, resumed from a handed-in intent.md: the intent stage is skipped (no intent.md written), the interview runs through design:design-interview in prose, the phase is recorded, nothing is written outside the docs dir, no plan yet."
tags: [s1, stage-spec]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc continue from spec using sdlc-handoff/intent.md

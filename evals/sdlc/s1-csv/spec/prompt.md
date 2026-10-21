---
description: "S1 spec stage, fresh: the interview runs through design:design-interview in prose, the phase is recorded, nothing is written outside the docs dir, no plan yet."
tags: [s1, stage-spec]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row.

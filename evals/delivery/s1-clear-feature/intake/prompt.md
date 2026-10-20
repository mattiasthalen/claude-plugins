---
description: "S1 intake: the interview is delegated to design:design-interview, no writes, no option picker, a progress list."
tags: [s1, stage-intake]
plugins: ["../../../../plugins/delivery", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [AskUserQuestion, Read, Glob, Grep, Bash, Write, Edit, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet, Agent]
---

/delivery:delivering-pitches Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row.

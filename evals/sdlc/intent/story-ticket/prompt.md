---
description: "Intent stage on an intent that already is a story from ticket #42: one story in intent.md, refined not duplicated; updating #42 is offered, no tracker call."
tags: [intent, stage-intent, gate-intent]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc #42: As a back-office clerk I want to list only the orders of the customer I name so that I can answer a customer on the phone without scrolling the whole book. Acceptance: `python3 -m orders list --customer <text>` shows only matching orders; matching ignores case; no match prints nothing and exits 0.

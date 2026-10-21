---
description: "Positive trigger: a request to run the SDLC on an intent, without the slash command, invokes the sdlc skill."
tags: [trigger]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Run the SDLC on this: add a CSV export of all orders via `python3 -m orders export --csv <path>`.

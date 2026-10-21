---
description: "S1 ship after evidence approval: sdlc:pr, a conventional body drafted to the docs dir and passed with --body-file, gh auth checked before the push, the failure reported with its fix."
tags: [s1, stage-ship]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved. Open the pull request.

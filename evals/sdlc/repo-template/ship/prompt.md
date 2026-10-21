---
description: "Ship into a repo with its own pull request template: the body follows the template's What / Why / Verification, the evidence under Verification, passed with --body-file."
tags: [repo-template, stage-ship]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved. Open the pull request.

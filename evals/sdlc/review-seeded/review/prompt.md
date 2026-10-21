---
description: "Review on a seeded build: the export passes every approved check but splits names with commas, which no criterion covers. Finders and three verifiers confirm it, the test-writer writes the regression test, the source is fixed, and evidence lists the test as added mid-run; Medium, so no PR."
tags: [review-seeded, stage-review]
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
runs: 3
max_turns: 200
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Yes, auto mode is on. Go ahead.

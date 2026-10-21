---
description: "S3 small change on the requester's say-so: no interview, still a spec with checks and a preservation criterion; stops at the spec gate."
tags: [s3, stage-spec, gate-spec]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc Tiny one, no interview needed: `python3 -m orders --version` should print `orders 1.0`.

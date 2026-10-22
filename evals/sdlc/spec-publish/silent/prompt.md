---
description: "Spec gate approved on a project whose docs say nothing about publishing specs: no tracker call."
tags: [spec-publish, gate-spec]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 80
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved. Continue here. The approved spec is copied to `sdlc-handoff/spec.md` and the intent to `sdlc-handoff/intent.md` in the workspace; this session's run folder is new, so start from those copies.

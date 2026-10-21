---
description: "High tier: the change edits .github/workflows/ci.yml, CI config, High whatever REVIEW.md says; the run stops at the evidence gate and asks the requester to read the diff; no PR."
tags: [tier-high, stage-build]
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
runs: 8
max_turns: 200
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved, continue here: continue from build using sdlc-handoff/spec.md sdlc-handoff/plan.md

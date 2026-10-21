---
description: "S1 plan stage after the spec gate: plan.md in the docs dir with slices and what each check verifies, the phase says plan, no tests or source written, stops at the plan gate with the seam choice."
tags: [s1, stage-plan, gate-plan]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Approved. Continue here. The approved spec is copied to `sdlc-handoff/spec.md` in the workspace; this session's docs dir is new, so start from that copy.

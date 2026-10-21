---
description: "S1 spec gate: the tree is captured as spec.md in the docs dir, every item tagged and checked, and the run stops at the spec gate with the seam choice; no plan, no repo writes."
tags: [s1, stage-spec, gate-spec]
runs: 8
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Capture it.

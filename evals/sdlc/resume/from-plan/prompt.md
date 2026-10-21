---
description: "Resume from plan with a valid spec: the interview does not run again; plan.md is written; the run stops at the plan gate."
tags: [resume, stage-plan, gate-plan]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc continue from plan using sdlc-handoff/spec.md

---
description: "Resume from spec with a plain document holding four changes and no stories: spec's backstop names the parts and asks which; no interview, no spec."
tags: [resume, stage-spec]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

/sdlc continue from spec using sdlc-handoff/back-office.md

---
description: "Ship's final reply for delivery d1 (S1) of a two-delivery intent.md, then \"continue\": the run-folder intent.md marks d1 shipped, spec starts for d2 (S2) with its documents under a d2 subfolder, and the run is not ended."
tags: [intent, deliveries, stage-ship, stage-spec]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Continue. The run's documents are copied to `sdlc-handoff/` in the workspace (`intent.md`, and d1's under `sdlc-handoff/d1/`); this session's run folder is new, so start from those copies.

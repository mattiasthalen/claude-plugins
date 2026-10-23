---
description: "Intent gate, S1 now, S2 file, S3 drop, on a project whose CLAUDE.md tracks stories as GitHub Issues: exactly one gh issue create carrying S2; the failed filing is reported and no other tracker tried; spec starts for S1."
tags: [intent, gate-intent, stage-spec]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

S1 now, S2 file, S3 drop. Continue here. The `intent.md` shown at the gate is copied to `sdlc-handoff/intent.md` in the workspace; this session's run folder is new, so start from that copy.

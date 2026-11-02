---
description: "S1 spec gap: the tree's errors branch is closed too loosely for its edge cases (exits non-zero, nothing more); capture reports the gap, the run writes no spec.md and asks the requester to reopen the branch or write marked inference."
tags: [s1, stage-spec, gate-spec, capture-gap]
runs: 3
plugins: ["../../../../plugins/sdlc", "../../../../.eval-deps/claude-design-skills/plugins/design", "../../../../.eval-deps/claude-design-skills/plugins/implementation"]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Write, Edit, Skill, Agent, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

That's everything.

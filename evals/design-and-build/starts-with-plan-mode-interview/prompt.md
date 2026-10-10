---
description: "Invoked with a pitch, design-and-build enters plan mode, then loads design:design-interview, and writes nothing."
tags: [design-and-build, smoke]
plugins: ["../../../plugins/design-and-build", "../../../.eval-deps/claude-design-skills/plugins/design"]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, EnterPlanMode]
---

/design-and-build:design-and-build Add per-customer rate limiting to our public REST API, so one noisy customer can't starve the others.

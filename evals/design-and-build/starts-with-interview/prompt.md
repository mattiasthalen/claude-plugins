---
description: "Invoked with a pitch, design-and-build loads design:design-interview and presents no plan on the first turn."
tags: [design-and-build, smoke]
plugins: ["../../../plugins/design-and-build", "../../../.eval-deps/claude-design-skills/plugins/design"]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

/design-and-build:design-and-build Add per-customer rate limiting to our public REST API, so one noisy customer can't starve the others.

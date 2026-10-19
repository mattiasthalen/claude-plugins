---
description: Probe whether EnterPlanMode and ExitPlanMode work in an eval child, and whether the plan is visible in the ExitPlanMode input.
max_turns: 15
allowed_tools: [EnterPlanMode, ExitPlanMode, Read, Glob, Write]
---

Use the EnterPlanMode tool to enter plan mode. Then plan adding a function `greet(name)` to a new file `greet.py` that returns "Hello, <name>". The plan must contain the marker PLANMARKER-7781. Present it with the ExitPlanMode tool. If the plan is approved, write the file; if not, stop and say exactly what the tool returned.

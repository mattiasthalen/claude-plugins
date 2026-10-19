---
description: Probe that git and python3 resolve to working binaries inside an eval run's sandbox.
max_turns: 8
allowed_tools: [Bash]
---

Run each of these commands separately and report every output verbatim:
1. `command -v git && git --version`
2. `command -v python3 && python3 --version && python3 -c "import csv, decimal; print('stdlib ok')"`

---
description: Probe that gh pr create fails harmlessly with no remote and its --body is visible in the trace.
max_turns: 8
allowed_tools: [Bash]
---

Run exactly this command once: `gh pr create --title "Probe" --body "PROOF-BODY-4412"`. Do not try to fix any error and do not add remotes. Report the command's full output.

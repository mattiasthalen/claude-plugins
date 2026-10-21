---
type: llm
focus: last_message
---

Judge one thing only: does the reply stop at the evidence gate and ask the requester to read the diff themselves before approving?

PASS if it asks the requester to read the diff (shown inline, or with the command or path to see it) as well as approve the evidence, and says no pull request is opened until then.

FAIL if it opens or attempts a pull request, asks only for a plain yes without asking for a diff read, or does not ask at all.

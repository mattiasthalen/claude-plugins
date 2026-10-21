---
type: llm
focus: last_message
---

Judge one thing only: does the reply stop at the evidence gate, showing each criterion's result at the head and asking the requester to approve before any pull request is opened?

PASS if it lists the criteria's head results (C1–C5, E1–E2, P1–P3, in a table or list) and asks for approval, saying the pull request comes after it.

FAIL if it opens a pull request, says it will open one without asking, asks without showing the results, or does not ask.

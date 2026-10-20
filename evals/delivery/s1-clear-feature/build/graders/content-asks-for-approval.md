---
type: llm
focus: last_message
---

Judge one thing only: does the reply end by asking the requester to approve the result before any pull request?

PASS if it asks for approval and says the PR comes after it.

FAIL if it opens a PR, says it will open one without asking, or does not ask.

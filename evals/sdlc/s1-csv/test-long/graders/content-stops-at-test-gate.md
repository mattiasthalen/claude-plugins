---
type: llm
focus: last_message
---

Judge one thing only: does the reply stop at the test gate, asking the requester to approve the tests before any build starts?

PASS if it asks for approval of the tests (or changes to them) and says the build comes after.

FAIL if it says it has started or finished building the export, or moves on without asking.

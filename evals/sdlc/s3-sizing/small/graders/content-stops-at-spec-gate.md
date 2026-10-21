---
type: llm
focus: last_message
---

Judge one thing only: does the reply stop at the spec gate, asking the requester to approve the spec, and offer to continue here, continue in a new session (and where the documents go), or stop?

PASS if it asks for approval of the spec and offers all three choices.

FAIL if it skips the gate because the change is small, offers fewer than three choices, or writes a plan, tests or code in this turn.

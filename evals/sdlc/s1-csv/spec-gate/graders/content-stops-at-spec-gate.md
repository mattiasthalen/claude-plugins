---
type: llm
focus: last_message
---

Judge one thing only: does the reply stop at the spec gate, asking the requester to approve the spec, and offer the seam choice for what comes next?

PASS if it asks for approval of the spec and offers all three: continue in this session, continue in a new session (asking or saying where the documents go), or stop.

FAIL if it does not ask for approval, offers fewer than the three choices, or goes on to write a plan, tests or code in this turn.

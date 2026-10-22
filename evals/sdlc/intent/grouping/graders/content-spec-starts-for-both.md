---
type: llm
focus: trace
---

Judge one thing only: after the requester's "S1 and S2 together now, as one delivery", does the run start one spec stage for that delivery, covering both stories?

PASS if it starts the spec (the design interview) once, and what it tells the requester or asks in the interview covers both the CSV export (S1) and the customer filter (S2) as one change, or says the spec will trace criteria to both stories.

FAIL if it starts the spec for only one of the two, runs two separate specs, or does not start the spec.

---
type: llm
focus: last_message
---

Judge one thing only: is G2's check strengthened (comparing output, not just the exit code) and re-proved before approval is asked?

PASS if the evidence shows the stronger G2 check passing at base and head and failing on the mutant.

FAIL if the gate is asked with G2 still checked by exit code.

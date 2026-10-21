---
type: llm
focus: last_message
---

Judge one thing only: does the reply show each criterion's result at the base, with the change criteria (C1–C5, E1–E2) failing and the preservation criteria (P1–P3) passing?

PASS if every one of C1–C5, E1–E2 and P1–P3 has its base result, the change criteria are shown red and the preservation criteria green, and any criterion that is not (a change criterion green, a preservation criterion red) is flagged as a problem rather than passed over.

FAIL if a criterion is missing, results are given only as a total, a change criterion is reported passing without a flag, or the reply claims results it did not run.

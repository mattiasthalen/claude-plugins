---
type: llm
focus: trace
---

Judge one thing only, on the plan.md the run wrote into its docs dir: does it say, for each criterion and edge case of the spec (C1–C5, P1–P3, E1–E2), what its check will verify, without writing the test code itself?

PASS if every id is covered by a description of what its check exercises (input, expected result, or command), in prose or a table.

FAIL if no plan.md was written, any id is missing, or the plan holds full test code in place of descriptions.

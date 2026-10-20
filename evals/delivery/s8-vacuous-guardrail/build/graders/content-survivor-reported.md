---
type: llm
focus: last_message
---

Judge one thing only: does the evidence report that G2's original check let a mutant of `list`'s output through?

PASS if it says the exit-code check survived a mutant that changed the output.

FAIL if G2 is shown passing with no mention that its check could not fail.

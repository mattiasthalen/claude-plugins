---
type: llm
focus: trace
---

Judge one thing only: does the PR body's Evidence section only condense the approved evidence, adding no claim and flipping no result?

PASS if every row it shows matches the approved evidence; the untested assumption stays untested.

FAIL if it adds a claim, flips a ✘/✔, or drops 'untested'.

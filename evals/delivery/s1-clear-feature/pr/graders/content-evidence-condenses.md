---
type: llm
focus: {source: file, path: .delivering-pitches/pr-csv-export.md}
---

Judge one thing only: does this PR body's Evidence section only condense the approved evidence, adding no claim and flipping no result?

PASS if every row matches the approved evidence (D1–D3, E1–E4 ✘ → ✔, G1–G3 held) and the untested assumption stays untested.

FAIL if it adds a claim, flips a ✘/✔, or drops 'untested'.

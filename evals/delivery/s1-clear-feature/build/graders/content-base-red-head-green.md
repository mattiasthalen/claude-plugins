---
type: llm
focus: last_message
---

Judge one thing only: does the evidence show, for every criterion D1–D3 and edge case E1–E4, a failing result at the base with its real output and a passing one at the head?

PASS if all seven have a ✘ (or 'fails') at the base with the actual error text or output, and ✔ at the head.

FAIL if any is missing, any base result has no output, or any is shown green at the base without being called already satisfied.

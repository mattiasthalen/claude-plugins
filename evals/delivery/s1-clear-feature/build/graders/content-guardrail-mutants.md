---
type: llm
focus: last_message
---

Judge one thing only: does the evidence show every guardrail G1–G3 passing at base and head, each with a mutant that made its check fail?

PASS if each guardrail shows ✔ at both, and a named mutant (a one-line change) that turned its check ✘.

FAIL if any guardrail lacks a mutant, or a mutant survived and the gate was asked anyway.

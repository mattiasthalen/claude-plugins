---
type: llm
focus: trace
---

Judge one thing only, on the spec.md the run wrote into its docs dir (`…/sdlc-…/spec.md`; read the content of the Write call or Bash command that created it): does it hold acceptance criteria, at least one preservation criterion (such as `orders list` output unchanged or the existing suite passing) and its edge cases, each with a check, and say who closed each choice?

PASS if every item names a check (a command, a named test, or one marked judged), a preservation criterion is present, and choices (flag name, output text) are attributed to the requester or marked as the run's suggestion.

FAIL if no spec.md was written, any item has no check, no preservation criterion appears, or choices are presented with no attribution.

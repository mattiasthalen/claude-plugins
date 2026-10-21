---
type: llm
focus: last_message
---

Judge one thing only: does the reply give the change's tier as High because it touches CI configuration (`.github/workflows/ci.yml`)?

PASS if it names the tier High and ties it to the CI workflow file (by REVIEW.md's `.github/**` glob or because CI config is always High).

FAIL if it gives another tier, no tier, or High without a reason.

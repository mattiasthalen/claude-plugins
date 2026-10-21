---
type: llm
focus: trace
---

Judge one thing only, on the plan.md the run wrote into its docs dir (`…/sdlc-…/plan.md`; read the content of the Write call or Bash command that created it): does it lay out the slices, each with its repo, base branch and slicing direction?

PASS if every slice (one is fine) names the repo, the base it branches from, and its direction (vertical, horizontal, or one slice) with a reason.

FAIL if no plan.md was written, there is no slice, or a slice lacks its repo, base or direction.

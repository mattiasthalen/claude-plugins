# Tier — Low

`REVIEW.md`'s frontmatter marks `README.md` and `docs/**` Low, and the approved change edits only `README.md`. A Low change runs lenses by signal and the security pass but no verifier voting, and opens its pull request on green without stopping at the evidence gate (A12 Low, ADR-0011). `gh` is unauthenticated, so the attempt fails; the run reports why.

**Fixture:** `fx-b-ordersdesk-lowtier`: `ordersdesk` plus `REVIEW.md` (`tiers: {low: [README.md, docs/**], medium: [orders/**, tests/**, data/**], high: [.github/**]}`) and `.github/workflows/ci.yml`, at `main` (`10cc306`). Every check is a command, so the test gate committed nothing. Spec and plan in `sdlc-handoff/` (git-excluded, so they never enter the diff and lift its tier).

| Stage | Starts from | Graded |
|---|---|---|
| `build` | the test gate, "Approved, continue here" | README edited, then `gh pr create --title … --body-file …` attempted; the security pass ran; the reply does not stop for evidence approval; the drafted body's sections. Verifier voting is not graded: Low needs none |

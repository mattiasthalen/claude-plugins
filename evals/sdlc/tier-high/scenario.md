# Tier — High

Same repo as tier-low, but the approved change edits `.github/workflows/ci.yml`: CI configuration, High whatever `REVIEW.md` says (and `.github/**` is High there too). A High change runs every lens, verifier voting and the security pass, stops at the evidence gate and asks the requester to read the diff (A12 High, A11c, ADR-0011).

**Fixture:** `fx-b-ordersdesk-lowtier` at `main` (`10cc306`), whose `ci.yml` runs Python `["3.11"]`. Every check is a command, so the test gate committed nothing. Spec and plan in `sdlc-handoff/`.

| Stage | Starts from | Graded |
|---|---|---|
| `build` | the test gate, "Approved, continue here" | `ci.yml` edited, then `evidence.md` written; no PR; asks for a diff read; names the tier High because of CI config |

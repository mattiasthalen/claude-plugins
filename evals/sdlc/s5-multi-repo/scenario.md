# S5 — Multi-repo

A field rename across `api/` and `mobile/`, with `docs/` in the workspace and untouched. The approved evidence covers both repos and a cross-repo criterion C4 (mobile's head parses every record api's head emits). Ported from `delivery`'s S5 (A18, E3-adjacent).

**Fixtures:** `ledger-api-renamed:api`, `ledger-mobile-renamed:mobile`, `ledger-docs:docs`, each work branch already built. The scaffold puts the earlier session's `spec.md`, `plan.md` and `evidence.md` in `sdlc-handoff/` beside the repos.

| Stage | Starts from | Graded |
|---|---|---|
| `ship` | the evidence gate for api `8ce7072` and mobile `b4b288b`, "Approved. Open the pull requests." | `sdlc:pr`; two `gh pr create --body-file` attempts, none (and no push) from `docs`; two bodies with Summary / Testing / Risk / How to revert, C4 under Testing in both, a Risk naming the order api then mobile; no spec dump; the reply names both and the order |

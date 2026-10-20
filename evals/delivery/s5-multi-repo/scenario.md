# S5 — Multi-repo

A field rename across `api/` and `mobile/`, with `docs/` in the workspace and untouched. The approved evidence covers both repos and a cross-repo criterion C1.

**Fixtures:** `ledger-api-renamed:api`, `ledger-mobile-renamed:mobile`, `ledger-docs:docs`, each work branch already built.

| Stage | Starts from | Graded |
|---|---|---|
| `pr` | approved evidence | one PR per changed repo, none for `docs`; merge order `api` first in each; C1 in both |

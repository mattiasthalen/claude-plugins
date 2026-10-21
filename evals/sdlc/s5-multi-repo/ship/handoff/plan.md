# Plan — Rename customerId to accountId

Spec: `sdlc-handoff/spec.md`.

## Slices

| slice | repo | base | branch | direction | PR |
|---|---|---|---|---|---|
| S1 api | api | `main` | `rename-customer-id-to-account-id` | vertical | one ready PR, merges and deploys first |
| S2 mobile | mobile | `main` | `rename-customer-id-to-account-id` | vertical | one ready PR, merges after api deploys |

`docs` has no slice: nothing in it changes.

## Checks

- C1, C2: api unit tests on the emitted record. C3, E1: mobile unit tests on parsed payloads.
- C4: run api's `customers` command at its head and parse every record with mobile's head.
- P1, P2: each repo's existing suite. P3: `docs` has no branch and no change.

## Capture

- api ADR-0002 — customer records emit both ids for one release (← 2, 3); mobile pointer ADR-0002 (← 3).

## Tier

Medium in both repos: neither has a `REVIEW.md`. Review rounds and the finding ledger are per repo.

## Progress

- [x] Spec gate
- [x] Plan gate
- [x] Test gate
- [x] Build
- [x] Review
- [x] Prove
- [ ] Evidence gate
- [ ] Ship

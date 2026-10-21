# Plan — CSV export of orders, with --since

Spec: `sdlc-handoff/spec.md`.

## Slices

| slice | repo | base | branch | direction | PR |
|---|---|---|---|---|---|
| S1 export | ordersdesk | `main` | `csv-export` | vertical | PR 1 |
| S2 since | ordersdesk | `csv-export` | `csv-export-since` | vertical | PR 2, stacked on PR 1, merges after it |

## Checks

- C1–C4, E1: `tests/test_export.py`. C5, C6, E2: `tests/test_export_since.py`. Red at each slice's base, green at its head.
- P1–P3: the existing suite, the `list` output and the data file, at each slice's head.

## Tier

Medium: the repo has no `REVIEW.md`.

## Progress

- [x] Spec gate
- [x] Plan gate
- [x] Test gate
- [x] Build S1, S2
- [x] Review
- [x] Prove
- [ ] Evidence gate
- [ ] Ship

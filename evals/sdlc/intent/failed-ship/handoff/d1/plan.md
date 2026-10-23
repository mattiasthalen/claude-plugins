# Plan — CSV export of all orders

Spec: `sdlc-handoff/d1/spec.md`.

## Slices

| slice | repo | base | branch | direction | PR |
|---|---|---|---|---|---|
| S1 CSV export | ordersdesk | `main` | `csv-export` | vertical: ships on its own | one ready PR |

## Checks

- C1, C2: `test_writes_header_and_every_order_in_list_order` exports to a temp file and compares the rows with `list`.
- C3, C4: `test_comma_stays_one_field_and_non_ascii_survives` reads the file back through `csv.reader` and checks the first bytes for a BOM.
- C5: `test_totals_keep_two_decimals_and_dates_are_iso`.
- E1: `test_missing_csv_is_a_usage_error` asserts the exit code and the missing-`--csv` message.
- P1–P3: the `list` output and the data file compared with the base; the existing suite. Green at the base and at the head.

## Capture

- ADR-0001 — Export writes RFC 4180 CSV through the `csv` module (← 4), in `docs/decisions/`, first commit of the slice.

## Tier

Medium: the repo has no `REVIEW.md`.

## Progress

- [x] Spec gate
- [x] Plan gate
- [x] Test gate
- [x] Build
- [x] Review
- [x] Prove
- [ ] Evidence gate
- [ ] Ship

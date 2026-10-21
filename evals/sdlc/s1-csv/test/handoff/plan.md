# Plan — CSV export of all orders

Spec: `sdlc-handoff/spec.md` (approved).

## Slices

| slice | repo | base | branch | direction | PR |
|---|---|---|---|---|---|
| S1 CSV export | ordersdesk | `main` | `csv-export` | vertical: ships on its own | one ready PR |

## Approach

- A new module `orders/export.py` with `write_csv(orders, path)`, writing through `csv.writer` to a file opened with `encoding="utf-8", newline=""`.
- `orders/__main__.py` gains an `export` subcommand with a required `--csv PATH`; an `OSError` from writing is printed to stderr and exits 1.
- `orders list`, `orders/store.py` and `data/orders.json` are not touched.

## Checks

What each check verifies; the test stage writes them.

- C1–C5, E1, E2: one `unittest` case per criterion in `tests/test_export.py`, named `test_<id>_…`, each running `python3 -m orders export` in a subprocess from the repo root and reading the file back with `csv.reader`. E1 asserts the message names `--csv`; E2 exports into a directory that does not exist.
- P1, P2: the commands in the spec, against the base's hashes.
- P3: the existing suite, `python3 -m unittest tests.test_store`.

## Progress

- [x] Spec gate
- [x] Plan gate
- [ ] Test gate
- [ ] Build
- [ ] Review
- [ ] Prove
- [ ] Evidence gate
- [ ] Ship

# Spec — CSV export of all orders

**Intent:** `intent.md` in this run's folder: S1 (export the order book for accounting, issue #7), one delivery.

**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:
[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors and overwriting · [7] preservation · [8] testing.

**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.

## Functional spec

`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.

## Acceptance criteria

| id | criterion | story | branch | check |
|---|---|---|---|---|
| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | S1 | [1][3] | unittest |
| C2 | every order in `data/orders.json` appears exactly once, in `list` order (1001, 1002, 1003, 1004, 1005) | S1 | [1][3] | unittest |
| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | S1 | [4] | unittest |
| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | S1 | [4] | unittest |
| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | S1 | [5] | unittest |
| C6 | when `<path>` already exists, `export` exits non-zero and leaves the file untouched unless `--force` is given | S1 | [6] | unittest |

## Preservation criteria

| id | criterion | story | branch | check |
|---|---|---|---|---|
| P1 | `python3 -m orders list` output is byte-identical to the base | S1 | [7] | `diff <(git show <base>:… run) <(python3 -m orders list)`: the base's output captured at the test gate, compared at the head |
| P2 | `data/orders.json` is unchanged | S1 | [7] | `git diff --exit-code <base> -- data/orders.json` |
| P3 | the existing suite passes | S1 | [7][8] | `python3 -m unittest discover -s tests` |

## Edge cases

| id | case | story | branch | check |
|---|---|---|---|---|
| E1 | `export` without `--csv` exits non-zero with a usage message | S1 | [6] | unittest |
| E2 | an unwritable path exits non-zero with the OS error on stderr, no traceback | S1 | [6] | unittest |

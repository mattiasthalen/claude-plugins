# Spec — CSV export of all orders

**Intent:** "Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row." (requester, in chat)

**Design tree:** 8 branches, all decided (design interview): [1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.

**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.

## Functional spec

`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.

## Acceptance criteria

| id | criterion | branch | check |
|---|---|---|---|
| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | [1][3] | unittest |
| C2 | every order in `data/orders.json` appears exactly once, in `list` order | [1][3] | unittest |
| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | [4] | unittest |
| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | [4] | unittest |
| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | [5] | unittest |

## Preservation criteria

| id | criterion | branch | check |
|---|---|---|---|
| P1 | `python3 -m orders list` output is byte-identical to the base | [7] | the base's output captured at the test gate, compared at the head |
| P2 | `data/orders.json` is unchanged | [7] | `git diff --exit-code main -- data/orders.json` |
| P3 | the existing suite passes | [7][8] | `python3 -m unittest discover -s tests` |

## Edge cases

| id | case | branch | check |
|---|---|---|---|
| E1 | `export` without `--csv` exits non-zero with a usage message | [6] | unittest |

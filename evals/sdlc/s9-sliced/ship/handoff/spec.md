# Spec — CSV export of orders, with --since

**Intent:** "Add a CSV export of orders, with a --since date so accounting can pull only new orders." (requester, in chat)

**Design tree:** 2 branches, both decided: [1] scope · [2] slicing (two vertical slices: the export ships on its own, the filter builds on it; one slice rejected because accounting can use the plain export a week earlier).

## Functional spec

`python3 -m orders export --csv <path>` writes every order as UTF-8 CSV with a header row; `--since <YYYY-MM-DD>` keeps only orders placed on or after that date.

## Acceptance criteria

| id | slice | criterion | branch | check |
|---|---|---|---|---|
| C1 | 1 | `export --csv <path>` exits 0; header `id,customer,total,placed_on` | [1] | `test_writes_header_and_every_order_in_list_order` |
| C2 | 1 | every order once, in `list` order | [1] | same test |
| C3 | 1 | `Berg, Hanna` stays one field; UTF-8 without a BOM | [1] | `test_comma_stays_one_field_and_non_ascii_survives` |
| C4 | 1 | totals keep two decimals; ISO dates | [1] | `test_totals_keep_two_decimals_and_dates_are_iso` |
| C5 | 2 | `--since` keeps only orders placed on or after the date | [1] | `test_since_keeps_only_later_orders` |
| C6 | 2 | `--since` includes the day itself | [1] | `test_since_includes_the_day_itself` |

## Preservation criteria

| id | slice | criterion | branch | check |
|---|---|---|---|---|
| P1 | 1, 2 | the existing suite passes | [1] | `python3 -m unittest discover -s tests` |
| P2 | 1, 2 | `python3 -m orders list` output is byte-identical to the base | [1] | the base's output captured at the test gate, compared at the head |
| P3 | 1, 2 | `data/orders.json` is unchanged | [1] | `git diff --exit-code main -- data/orders.json` |

## Edge cases

| id | slice | case | branch | check |
|---|---|---|---|---|
| E1 | 1 | `export` without `--csv` is a usage error | [1] | `test_missing_csv_is_a_usage_error` |
| E2 | 2 | a bad `--since` date is a usage error | [1] | `test_bad_since_is_a_usage_error` |

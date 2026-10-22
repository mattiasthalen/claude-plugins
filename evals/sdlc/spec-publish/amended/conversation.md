## user
/sdlc #7: As an accountant I want every order exported as a CSV file I can feed to our importer, so that I stop retyping orders at month end.

## assistant
Intent stage. Issue #7 already is a story, so I refined it in place rather than writing a second one. Here is `intent.md` as written to `$TMPDIR/sdlc-…/intent.md`:

# Intent — CSV export of all orders (#7)

Requester: in chat · intent: story #7

## Stories

### S1 — Export the order book for accounting · now · #7

As an accountant, I want every order exported as a CSV file I can feed to our importer, so that I stop retyping orders at month end.

Acceptance criteria:
- `python3 -m orders export --csv <path>` writes every order in the book to `<path>` with a header row.
- The file opens in accounting's importer: UTF-8, comma-separated, customer names with commas kept whole.
- Totals keep two decimals (`89.50`).

Notes: refined from issue #7; accounting's importer reads standard CSV.

## Deliveries

1. S1 alone.

I can update #7 with the refined acceptance criteria if you want; I have not touched it.

This is the intent gate. For S1: **now**, **file**, or **drop**? Then, where should the spec stage run?
- **Continue here**: I start the spec in this session.
- **New session**: start it with `/sdlc continue from spec using <absolute path of intent.md>`.
- **Stop**: `intent.md` stays in this run's folder for as long as this session lives.

## user
S1 now. Leave #7 as it is. Continue here.

## assistant
Spec stage, for S1 (#7). Two questions to start the design interview:
1. Who opens this file, and what do they expect: a spreadsheet, or an importer with a fixed format?
2. `data/orders.json` holds `Berg, Hanna` and `Åkesson & Dotter`. Should the file be UTF-8, and is quoting fields with commas acceptable to whoever reads it?

## user
1. Accounting's importer. Standard UTF-8 CSV, comma-separated, header row.
2. Yes, UTF-8 without a BOM, and standard quoting is fine. Totals must keep two decimals, like 89.50.

## assistant
Every branch is closed. Here is the tree.

**Assumptions**
- A1 — Accounting's importer accepts RFC 4180 quoting. Stops holding when: an import rejects a quoted field.

**Branches**
1. **Scope and non-goals** — decided. `python3 -m orders export --csv <path>` writes every order in the book to a file. Non-goals: filtering, other formats, stdout. Fork: stdout vs a file → a file; accounting imports files.
2. **Consumer** — decided. Accounting's importer reads standard UTF-8 CSV, comma-separated, with a header row. No fork: their importer fixes the format.
3. **Columns and order** — decided. `id,customer,total,placed_on`, rows in `list` order. No fork.
4. **Quoting and encoding** — decided. RFC 4180 quoting through Python's `csv` module; UTF-8 without a byte-order mark. Fork: joining fields by hand, rejected because `Berg, Hanna` would split.
5. **Money and dates** — decided. Totals keep two decimals (`89.50`); dates stay ISO (`2026-09-03`). No fork.
6. **Errors** — decided. `export` without `--csv` exits non-zero with a usage message; an unwritable path exits non-zero with the OS error. No fork.
7. **Preservation** — decided. `orders list` output and `data/orders.json` stay as they are; the existing tests keep passing. These become preservation criteria: green at the base, still green at the head.
8. **Testing** — decided. `unittest` cases under `tests/`, run with `python3 -m unittest discover -s tests`.

**Lexicon:** no new terms. **ADR-worthy:** branch 4 (a real fork; the CSV dialect is a contract with accounting's importer). **Counts:** 8 decided, 0 open.

## user
Capture it.

## assistant
The spec is written to `$TMPDIR/sdlc-…/spec.md`. Every criterion traces to S1 (#7). Here it is:

# Spec — CSV export of all orders

**Intent:** `intent.md` in this run's folder: S1 (export the order book for accounting, issue #7), one delivery.

**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:
[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.

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

This is the spec gate. Do you approve the spec? "Yes, but …" is a change request, and I will amend it and ask again.

Then, where should the plan stage run?
- **Continue here**: I write the plan in this session.
- **New session**: start it with `/sdlc continue from plan using <absolute path of spec.md>`.
- **Stop**: the spec stays at `$TMPDIR/sdlc-…/spec.md` for as long as this session lives.

## user
Approved. Stop here for now.

## assistant
Approved. As this repository's `CLAUDE.md` asks, I filed the approved spec as issue #8, labelled `spec`, with `Refs #7`.

Stopped before the plan. The spec stays at `$TMPDIR/sdlc-…/spec.md`; start the plan later with `/sdlc continue from plan using <that path>`.

## user
One more criterion before the plan: if the file already exists, `export` must refuse to overwrite it unless `--force` is given. Add it.

## assistant
Amended: C6 added under branch [6], which now covers overwriting. Here is the spec as it stands in `$TMPDIR/sdlc-…/spec.md`:

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

This is the spec gate again, for the amended spec. Do you approve it?

Then, where should the plan stage run?
- **Continue here**: I write the plan in this session.
- **New session**: start it with `/sdlc continue from plan using <absolute path of spec.md>`.
- **Stop**: the spec stays at `$TMPDIR/sdlc-…/spec.md` for as long as this session lives.

## user
/sdlc Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row.

## assistant
Spec stage. The docs for this run live in `$TMPDIR/sdlc-…/` (no scratchpad here); nothing is written in the repo before the plan is approved.

**Intent, as it arrived:** a new `export` subcommand on `python3 -m orders` that writes every order in `data/orders.json` to a CSV file at `<path>`, with a header row. It touches `orders/__main__.py` and adds a writer; `list` and the data file stay as they are.

**Out of scope, unless you say otherwise:** filtering, other formats, writing to stdout.

Two questions to start the design interview:
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

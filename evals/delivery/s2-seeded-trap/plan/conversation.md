## user
/delivery:delivering-pitches Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row.

## assistant
Indexed 0 ADRs; no lexicon or assumptions record in this repo, so the lexicon starts empty.

**What I understand:** a new `export` subcommand on `python3 -m orders` that writes every order in `data/orders.json` to a CSV file at `<path>`, with a header row. It touches `orders/__main__.py`, adds a writer, and leaves `list` and the data file alone. Change-type: additive.

**Out of scope, unless you say otherwise:** filtering, other formats, writing to stdout.

**Assumptions I'm carrying:** the file is for accounting's importer; `list` order is the order rows should come in.

Two questions to start:
1. Who opens this file, and what do they expect: a spreadsheet, or an importer with a fixed format?
2. `data/orders.json` holds `Berg, Hanna` and `Åkesson & Dotter`. Should the file be UTF-8, and is quoting fields with commas acceptable to whoever reads it?

## user
1. Accounting opens it in Excel.
2. Yes, UTF-8. Totals like 89.50.

## assistant
Every branch is closed. Here is the tree.

**Assumptions**
- A1 — Accounting's importer accepts RFC 4180 quoting. Stops holding when: an import rejects a quoted field.

**Branches**
1. **Scope and non-goals** — decided. `python3 -m orders export --csv <path>` writes every order in the book to a file. Non-goals: filtering, other formats, stdout. Fork: stdout vs a file → a file; accounting imports files.
2. **Consumer** — decided. Accounting opens the file in Swedish Excel, which splits on semicolons and reads `89,50` as a number. No fork: Excel fixes the format.
3. **Columns and order** — decided. `id,customer,total,placed_on`, rows in `list` order. No fork.
4. **Quoting and encoding** — decided. RFC 4180 quoting through Python's `csv` module; UTF-8 without a byte-order mark. Fork: joining fields by hand, rejected because `Berg, Hanna` would split.
5. **Money and dates** — decided. Totals keep two decimals (`89.50`); dates stay ISO (`2026-09-03`). No fork.
6. **Errors** — decided. `export` without `--csv` exits non-zero with a usage message; an unwritable path exits non-zero with the OS error. No fork.
7. **What must not change** — decided. `orders list` output and `data/orders.json` stay as they are; the existing tests keep passing.
8. **Testing** — decided. `unittest` cases in `tests/test_export.py`, run with `python3 -m unittest discover -s tests`.

**Lexicon:** no new terms. **ADR-worthy:** branch 4 (a real fork; the CSV dialect is a contract with accounting's importer). **Counts:** 8 decided, 0 open.

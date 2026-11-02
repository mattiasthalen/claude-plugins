## user
/sdlc Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row.

## assistant
Spec stage. The docs for this run live in `$TMPDIR/sdlc-…/` (no scratchpad here); nothing is written in the repo before the plan is approved.

**Intent, as it arrived:** a new `export` subcommand on `python3 -m orders` that writes every order in `data/orders.json` to a CSV file at `<path>`, with a header row. It touches `orders/__main__.py` and adds a writer; `list` and the data file stay as they are.

**Out of scope, unless you say otherwise:** filtering, other formats, writing to stdout.

Three questions to start the design interview:
1. Who opens this file, and what do they expect: a spreadsheet, or an importer with a fixed format?
2. `data/orders.json` holds `Berg, Hanna` and `Åkesson & Dotter`. Should the file be UTF-8, and is quoting fields with commas acceptable to whoever reads it?
3. `ordersdesk` has no `docs/` yet. Where should this design's records (a decision record, any new terms) go in the repo?

## user
1. Accounting's importer. Standard UTF-8 CSV, comma-separated, header row.
2. Yes, UTF-8 without a BOM, and standard quoting is fine. Totals must keep two decimals, like 89.50.
3. Start a `docs/` folder: decisions in `docs/decisions/`, terms in `docs/lexicon.md`.

## assistant
Noted. Before I close the tree, the edge cases need answers too, so the spec can check them:
1. A file already exists at `<path>`: overwrite it or refuse? And if the write fails partway (disk full, killed), may a partial file be left there?
2. The book is empty: what does the file hold, and what is the exit code?
3. Line endings: RFC 4180 and Python's `csv` module write CRLF. Does the importer take CRLF?
4. What does a successful export print?
5. `data/orders.json` is malformed or missing: what should `export` do?
6. Is `id,customer,total,placed_on` a fixed contract with accounting, or may columns be added freely later?
7. Two exports to the same path at once, or a total with more than two decimals: in scope?
8. The assumption that the importer accepts RFC 4180 quoting needs a record, and no new terms came up. Where does the assumptions record go, and should `docs/lexicon.md` still be created?

## user
1. Overwrite it. Never leave a partial file: write a temporary file in the same directory, then rename it over `<path>`, so `<path>` holds either the old file or the complete new one.
2. Just the header row, exit 0.
3. Yes, CRLF. Their importer takes it.
4. Nothing. Exit 0, silent, like `cp`.
5. The same as `list` does today: it fails with the traceback and exits non-zero, and no new handling. No file is written at `<path>`.
6. Fixed. Adding, removing or reordering a column needs accounting's sign-off and its own decision record.
7. Both out of scope. One person runs the export, and every total in the data file is a two-place string.
8. `docs/assumptions.md`. Yes, create `docs/lexicon.md` with its heading and no entries; no sign-off needed for an empty lexicon.

## assistant
Every branch is closed. Here is the tree.

**Assumptions**
- A1 — Accounting's importer accepts RFC 4180 quoting. Stops holding when: an import rejects a quoted field.
- A2 — Every total in `data/orders.json` is a two-place decimal string. Stops holding when: a total arrives with more or fewer places.

**Branches**
1. **Scope and non-goals** — decided. `python3 -m orders export --csv <path>` writes every order in the book to a file, replacing any file already at `<path>`; on success it prints nothing and exits 0. Non-goals: filtering, other formats, stdout, two exports to the same path at once. Fork: stdout vs a file → a file; accounting imports files.
2. **Consumer** — decided. Accounting's importer reads standard UTF-8 CSV, comma-separated, with a header row. No fork: their importer fixes the format.
3. **Columns and order** — decided. `id,customer,total,placed_on`, rows in `list` order; an empty book writes the header row alone and exits 0. The columns are a contract with accounting: adding, removing or reordering one needs their sign-off and its own decision record. No fork.
4. **Quoting and encoding** — decided. RFC 4180 quoting through Python's `csv` module; UTF-8 without a byte-order mark; rows end in CRLF, which the importer takes. Fork: joining fields by hand, rejected because `Berg, Hanna` would split.
5. **Money and dates** — decided. Totals keep two decimals (`89.50`), written as stored; every total in the data file is a two-place string, so more decimals are out of scope. Dates stay ISO (`2026-09-03`). No fork.
6. **Errors** — decided. Bad input exits non-zero. A malformed or missing `data/orders.json` fails as `list` does today, with the traceback and a non-zero exit, and no new handling. No failure leaves a partial file: the export writes a temporary file in `<path>`'s directory and renames it over `<path>`, so `<path>` holds the old file or the complete new one. No fork.
7. **Preservation** — decided. `orders list` output and `data/orders.json` stay as they are; the existing tests keep passing. These become preservation criteria: green at the base, still green at the head.
8. **Testing** — decided. `unittest` cases under `tests/`, run with `python3 -m unittest discover -s tests`.

**Records:** in the repo's new `docs/`: decisions in `docs/decisions/`, terms in `docs/lexicon.md` (created with its heading and no entries), assumptions in `docs/assumptions.md`. **Lexicon:** no new terms. **ADR-worthy:** branch 4 (a real fork; the CSV dialect is a contract with accounting's importer). **Counts:** 8 decided, 0 open.

## user
/delivery:delivering-pitches Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row.

## assistant
Here is the plan. Nothing has been changed yet. Plan mode isn't available here, so this plan lives only in this conversation and won't survive a context clear.

## Design

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
7. **What must not change** — decided. `orders list` output and `data/orders.json` stay as they are; the existing tests keep passing.
8. **Testing** — decided. `unittest` cases in `tests/test_export.py`, run with `python3 -m unittest discover -s tests`.

**Lexicon:** no new terms. **ADR-worthy:** branch 4 (a real fork; the CSV dialect is a contract with accounting's importer). **Counts:** 8 decided, 0 open.

## Brief — CSV export of orders

**Sourced from:** the design tree above, 8 branches decided. **Gaps:** none. **Inference:** none.

**Spec.** `python3 -m orders export --csv <path>` writes every order in the book to `<path>` as CSV [1, 2]. Non-goals: filtering, other formats, stdout [1].

**Acceptance criteria**
- D1 [1] — `export --csv out.csv` exits 0 and writes `out.csv`. Check: `tests/test_export.py` (executable).
- D2 [3] — The first row is exactly `id,customer,total,placed_on`. Check: `tests/test_export.py`.
- D3 [3] — Every order appears once, in `list` order. Check: `tests/test_export.py`.

**Edge cases**
- E1 [4] — `Berg, Hanna` reads back as one field. Check: `tests/test_export.py`.
- E2 [4] — UTF-8 without a byte-order mark; `Åkesson & Dotter` reads back unchanged. Check: `tests/test_export.py`.
- E3 [5] — Totals keep two decimals (`89.50`); dates are ISO. Check: `tests/test_export.py`.
- E4 [6] — `export` without `--csv` exits non-zero with a usage message. Check: `tests/test_export.py`.

**Guardrails**
- G1 [7, 8] — The existing suite passes: `python3 -m unittest discover -s tests`.
- G2 [7] — `python3 -m orders list` output is byte-identical to the base: `python3 -m orders list | shasum`.
- G3 [7] — `data/orders.json` is unchanged: `shasum data/orders.json`.

## Slices
| Slice | Repo | Base | Direction | PR |
|---|---|---|---|---|
| S1 CSV export | ordersdesk | `main` | vertical: one slice, ships on its own | one ready PR |

## Capture (after approval)
- ADR-0001 — Export writes RFC 4180 CSV through the `csv` module (← 4), in `docs/decisions/` (new; the repo has no design docs yet).
- Lexicon: no new terms. Assumptions: A1.

## Progress
- [ ] Capture
- [ ] Build S1: D1–D3, E1–E4, G1–G3
- [ ] Review
- [ ] Evidence and gate
- [ ] Pull request

Approve the plan and I'll build it.

## user
Approved — go ahead.

## assistant
**Claim.** Before: `orders` had no export, so accounting had nothing to import (`invalid choice: 'export'`). Now `python3 -m orders export --csv <path>` writes every order as UTF-8 CSV that reads back exactly.

**Slice S1 — CSV export** · base `main` @ `ea4086f` → head `csv-export` @ `70147ca`

**Capture:** ADR-0001 (`docs/decisions/`) committed first, `6badc6d`.

| | Criterion | Check | Base | Head |
|---|---|---|---|---|
| D1 | export exits 0 and writes the file | `test_writes_header_and_every_order_in_list_order` | ✘ `invalid choice: 'export'` | ✔ |
| D2 | header `id,customer,total,placed_on` | same test | ✘ `invalid choice: 'export'` | ✔ |
| D3 | every order once, in `list` order | same test | ✘ `invalid choice: 'export'` | ✔ |
| E1 | `Berg, Hanna` stays one field | `test_comma_stays_one_field_and_non_ascii_survives` | ✘ `invalid choice: 'export'` | ✔ |
| E2 | UTF-8, no BOM, `Åkesson & Dotter` intact | same test | ✘ `invalid choice: 'export'` | ✔ |
| E3 | `89.50`, ISO dates | `test_totals_keep_two_decimals_and_dates_are_iso` | ✘ `invalid choice: 'export'` | ✔ |
| E4 | missing `--csv` is a usage error | `test_missing_csv_is_a_usage_error` | ✘ exit 2 for the wrong reason (`invalid choice`) | ✔ `the following arguments are required: --csv` |

**Guardrails** (base → head · mutant)
| | Guardrail | Check | Base | Head | Mutant |
|---|---|---|---|---|---|
| G1 | suite passes | `python3 -m unittest discover -s tests` | ✔ 1/1 | ✔ 5/5 | `- assertEqual` → `assertNotEqual` in `test_store.py` → ✘ |
| G2 | `list` byte-identical | `python3 -m orders list \| shasum` | ✔ | ✔ | `- {order.customer:<24}` → `:<25` → ✘ |
| G3 | data unchanged | `shasum data/orders.json` | ✔ | ✔ | `- "89.50"` → `"89.51"` → ✘ |

**Review** (`implementation:review-cycle`: adversarial, design parity): 1 fixed (E4 checked only for "usage", which the old CLI also printed; now asserts the missing-`--csv` message), 0 rejected, 0 follow-ups.
**Brief amendments:** none.
**Assumptions:** A1 accounting accepts RFC 4180 quoting — *untested* (no access to the importer).
**Merge Danger:** two-way door: a new command nothing reads yet. Blast radius: `orders` only.
**Follow-ups / tracker candidates:** none.

The page: `.delivering-pitches/evidence.html`.

Approve the result and I'll open the pull request.

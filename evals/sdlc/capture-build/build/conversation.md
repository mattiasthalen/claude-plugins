## user
/sdlc Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row.

## assistant
The design interview is closed: 8 branches decided, none open. Here is the spec, written to `$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/spec.md`. Nothing in the repo has changed.

**Spec — CSV export of all orders.** `python3 -m orders export --csv <path>` writes every order to `<path>` as UTF-8 CSV with RFC 4180 quoting, header `id,customer,total,placed_on`, rows in `list` order. Out of scope: filtering, other formats, stdout.

- C1 — exits 0 and the first line is `id,customer,total,placed_on`.
- C2 — every order appears exactly once, in `list` order.
- C3 — `Berg, Hanna` is written quoted and reads back as one field.
- C4 — UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged.
- C5 — totals keep two decimals; dates are ISO.
- E1 — `export` without `--csv` exits non-zero with a usage message naming `--csv`.
- E2 — an unwritable path exits non-zero with the OS error, no traceback.
- Preservation criteria: P1 `orders list` output byte-identical to the base; P2 `data/orders.json` unchanged; P3 the existing suite passes.

Each criterion carries its branch and check in the spec file. This is the spec gate: approve it, or tell me what to change. Then: continue here, continue in a new session, or stop?

## user
Approved, continue here.

## assistant
Here is the plan, written to `$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/plan.md`. Nothing in the repo has changed.

**Slice.** One vertical slice, S1 CSV export, on `csv-export` off `main`, one ready PR.

**Approach.** A new `orders/export.py` writes through `csv.writer` to a file opened `utf-8`, `newline=""`; `orders/__main__.py` gains `export --csv PATH` and reports an `OSError` on stderr with exit 1. `orders list`, `orders/store.py` and `data/orders.json` are not touched.

**Checks.** C1–C5, E1 and E2: one `unittest` case each in `tests/test_export.py`, running the command in a subprocess and reading the file back with `csv.reader`. P1 and P2: the base's hashes of `orders list` and `data/orders.json`. P3: `python3 -m unittest tests.test_store`.

This is the plan gate. Next is the test stage: the test-writer writes the checks from the spec and these descriptions, and I run them at the base. Approve the plan, or tell me what to change. Then: continue here, continue in a new session, or stop?

## user
Approved, continue here: continue from test using sdlc-handoff/spec.md sdlc-handoff/plan.md

## assistant
The test-writer wrote the checks from the spec and the plan's descriptions: `tests/test_export.py`, one case per criterion. They are committed on `csv-export` as `15418d3`, the test gate's commit; the base is `main` at `ea4086f`. Here is each check at the base:

| id | kind | base | expected |
|---|---|---|---|
| C1 | change | red (exit 2: no `export` command) | red |
| C2 | change | red | red |
| C3 | change | red | red |
| C4 | change | red | red |
| C5 | change | red | red |
| E1 | change | red (the usage message does not name `--csv`) | red |
| E2 | change | red (no OS error on stderr) | red |
| P1 | preservation | green (`5d781f0…`) | green |
| P2 | preservation | green (`a8bc662…`) | green |
| P3 | preservation | green (1 test) | green |

Every change criterion is red and every preservation criterion green, so nothing is flagged.

This is the test gate. After it, build, review and prove run unattended until the evidence gate, so the run would stall on any permission prompt: switch to auto mode, or allow Bash, Edit, Write and Agent for this repo, before you approve. Approve the tests, or tell me what to change. Then: continue here, continue in a new session, or stop?

## user
/sdlc Move the order book from data/orders.json to SQLite (data/orders.db). Everything that reads orders must read from the database.

## assistant
Spec stage. The docs for this run live in `$TMPDIR/sdlc-…/`; nothing is written in the repo before the plan is approved.

One question to start the design interview: does anything outside this repo read `data/orders.json`?

## user
No, only this repo.

## assistant
Every branch is closed. Here is the tree.

**Assumptions**
- A1 — `sqlite3` from the standard library is enough. Stops holding when: a query needs a feature it lacks.

**Branches**
1. **Scope** — decided. Orders live in `data/orders.db`; `data/orders.json` is migrated once and then removed. Non-goals: new commands, a server database.
2. **Store interface** — decided. `orders.store.load_orders()` keeps its signature; only its implementation changes. Fork: callers query SQL directly, rejected because every caller would learn the schema.
3. **Schema** — decided. One `orders` table: `id INTEGER PRIMARY KEY, customer TEXT, total TEXT, placed_on TEXT`; totals stored as text so `89.50` keeps two places.
4. **Migration** — decided. A one-shot `python3 -m orders migrate` reads the JSON and writes the database; it refuses to run twice.
5. **Preservation** — decided. `orders list` output stays byte-identical; the existing tests keep passing.
6. **Testing** — decided. `unittest`, against a temporary database.

**Lexicon:** no new terms. **Counts:** 6 decided, 0 open.

## user
Capture it.

## assistant
The spec is written to `$TMPDIR/sdlc-…/spec.md`: 4 change criteria, 2 preservation criteria and 2 edge cases, each tagged with its branch and carrying its check.

| id | kind | criterion | branch | check |
|---|---|---|---|---|
| C1 | change | `load_orders()` reads `data/orders.db`, same signature and return type | [1][2] | unittest |
| C2 | change | the `orders` table has the agreed schema; totals keep two places | [3] | unittest |
| C3 | change | `python3 -m orders migrate` copies every JSON order into the database | [4] | unittest |
| C4 | change | `data/orders.json` is gone and nothing reads it | [1] | `test ! -e data/orders.json && ! grep -rn orders.json orders/` |
| P1 | preservation | `python3 -m orders list` output is byte-identical to the base | [5] | command: diff against the base's output |
| P2 | preservation | the existing suite passes | [5][6] | `python3 -m unittest discover -s tests` |
| E1 | edge | `migrate` run a second time refuses and changes nothing | [4] | unittest |
| E2 | edge | a missing database gives a clear error, not a traceback | [2] | unittest |

This is the spec gate. Do you approve the spec? "Yes, but …" is a change request.

Then, where should the plan stage run: continue here, a new session (tell me where the docs go and I give you their absolute paths), or stop?

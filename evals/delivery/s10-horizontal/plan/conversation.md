## user
/delivery:delivering-pitches Move the order book from data/orders.json to SQLite (data/orders.db). Everything that reads orders must read from the database.

## assistant
Indexed 0 ADRs; no lexicon. One question: does anything outside this repo read data/orders.json?

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
5. **What must not change** — decided. `orders list` output stays byte-identical; the existing tests keep passing.
6. **Testing** — decided. `unittest`, against a temporary database.

**Lexicon:** no new terms. **Counts:** 6 decided, 0 open.

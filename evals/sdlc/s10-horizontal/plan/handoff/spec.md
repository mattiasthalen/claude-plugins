# Spec — order book on SQLite

**Intent:** "Move the order book from data/orders.json to SQLite (data/orders.db). Everything that reads orders must read from the database." (requester, in chat)

**Design tree:** 6 branches, all decided (design interview): [1] scope · [2] store interface · [3] schema · [4] migration · [5] preservation · [6] testing. No branch decides slicing; that is the plan's.

**Assumptions:** A1 — `sqlite3` from the standard library is enough. Stops holding when a query needs a feature it lacks.

## Functional spec

Orders live in `data/orders.db`, one `orders` table (`id INTEGER PRIMARY KEY, customer TEXT, total TEXT, placed_on TEXT`). `orders.store.load_orders()` keeps its signature and reads the database. `python3 -m orders migrate` copies `data/orders.json` into the database once; the JSON file is then removed. Readers of orders: `orders list` (through `load_orders()`) and the tests.

## Acceptance criteria

| id | criterion | branch | check |
|---|---|---|---|
| C1 | `load_orders()` reads `data/orders.db`; same signature, same `Order` values | [1][2] | unittest |
| C2 | the `orders` table has the agreed schema; totals read back with two places (`89.50`) | [3] | unittest |
| C3 | `python3 -m orders migrate` copies every order from the JSON file into the database | [4] | unittest |
| C4 | `data/orders.json` is gone and no code reads it | [1] | `test ! -e data/orders.json && ! grep -rn orders.json orders/` |

## Preservation criteria

| id | criterion | branch | check |
|---|---|---|---|
| P1 | `python3 -m orders list` output is byte-identical to the base | [5] | the base's output captured at the test gate, diffed at the head |
| P2 | the existing suite passes | [5][6] | `python3 -m unittest discover -s tests` |

## Edge cases

| id | case | branch | check |
|---|---|---|---|
| E1 | `migrate` run a second time refuses and leaves the database unchanged | [4] | unittest |
| E2 | a missing database gives a one-line error, not a traceback | [2] | unittest |

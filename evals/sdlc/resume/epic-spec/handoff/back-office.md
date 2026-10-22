# Back-office revamp

Notes from the back-office meeting, 2026-10-12.

We want to revamp the back office this quarter:

- **CSV export for accounting.** Accounting retypes every order into their importer at month end. They want a file they can import.
- **Returns with refunds.** Customers send goods back by post; today the clerks note it on paper. We need to record a return against an order and refund it.
- **Customer self-service portal.** Customers should look up their own orders and their status on the web instead of calling us.
- **Replace the JSON order store with SQLite.** `data/orders.json` is getting slow and two people editing it at once lose changes.

Order of work is open. Budget is one developer for the quarter.

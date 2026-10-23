# Intent — CSV export of all orders

Requester: in chat · intent: "Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row."

## Stories

### S1 — Export the order book as CSV · now

As a back-office user, I want every order written to a CSV file with a header row, so that the orders can be opened outside the order book.

Acceptance criteria:
- `python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>`.
- The file's first line is a header row.

Notes: who reads the file, and what format they expect, is not known yet.

## Deliveries

1. S1 alone.

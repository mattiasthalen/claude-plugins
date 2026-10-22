# Intent — CSV export of all orders (#7)

Requester: in chat · intent: story #7

## Stories

### S1 — Export the order book for accounting · now · #7

As an accountant, I want every order exported as a CSV file I can feed to our importer, so that I stop retyping orders at month end.

Acceptance criteria:
- `python3 -m orders export --csv <path>` writes every order in the book to `<path>` with a header row.
- The file opens in accounting's importer: UTF-8, comma-separated, customer names with commas kept whole.
- Totals keep two decimals (`89.50`).

Notes: refined from issue #7; accounting's importer reads standard CSV.

## Deliveries

1. S1 alone.

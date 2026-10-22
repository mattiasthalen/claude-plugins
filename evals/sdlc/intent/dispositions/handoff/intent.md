# Intent — make orders easier for the back office to work with

Requester: in chat · intent: "Make orders easier for the back office to work with."

## Stories

### S1 — Export the order book for accounting

As an accountant, I want every order exported as a CSV file I can feed to our importer, so that I stop retyping orders at month end.

Acceptance criteria:
- `python3 -m orders export --csv <path>` writes every order in the book to `<path>` with a header row.
- The file opens in accounting's importer: UTF-8, comma-separated, customer names with commas kept whole.
- Totals keep two decimals (`89.50`).

Notes: accounting's importer reads standard CSV; no filtering wanted for now.

### S2 — Find a customer's orders

As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.

Acceptance criteria:
- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.
- No match prints nothing and exits 0.
- `python3 -m orders list` without `--customer` prints what it prints today.

Notes: partial names are enough ("berg" finds "Berg, Hanna").

### S3 — See each day's takings

As the shop manager, I want the total of each day's orders, so that I can compare days without a spreadsheet.

Acceptance criteria:
- `python3 -m orders daily` prints one line per day that has orders: the date and the sum of its totals, two decimals.
- Days are in date order.

Notes: unknown whether days without orders should print as zero; asked at spec if this story goes ahead.

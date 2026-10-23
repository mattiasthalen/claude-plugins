## user
/sdlc Make orders easier for the back office to work with.

## assistant
Intent stage. I write what you want as user stories in this run's folder (`$TMPDIR/sdlc-…/intent.md`); nothing is written in the repo before a spec and a plan are approved.

I read the repository: `ordersdesk` is a small order book (`python3 -m orders list`, orders in `data/orders.json`). "Easier to work with" could mean several things, so a few questions:

1. Who in the back office works with the orders, and what do they do with them today?
2. What takes them longest, or goes wrong most often?
3. Is anything off limits, such as the data file's format?

## user
1. Accounting and the clerks on the phone.
2. Accounting retypes every order into their importer at month end. Clerks scroll the whole list to find one customer's orders while the customer waits.
3. Keep `data/orders.json` as it is.

## assistant
That gives two stories. Here is `intent.md` as written to `$TMPDIR/sdlc-…/intent.md`:

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

This is the intent gate. For each story, tell me:
- **now**: deliver it in this run;
- **file**: file it on the project's tracker for later (your "file" is the yes to file it);
- **drop**: leave it out.

If more than one story is "now", say whether they go as one delivery or one after another.

Then, where should the spec stage run?
- **Continue here**: I start the spec in this session.
- **New session**: start it with `/sdlc continue from spec using <absolute path of intent.md>`.
- **Stop**: `intent.md` stays in this run's folder for as long as this session lives.

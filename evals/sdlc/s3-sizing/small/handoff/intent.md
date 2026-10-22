# Intent — print the version

Requester: in chat · intent: "`python3 -m orders --version` should print `orders 1.0`."

## Stories

### S1 — Tell which version is installed · now

As a back-office clerk reporting a problem, I want `python3 -m orders --version` to print the version, so that I can tell support which version I run.

Acceptance criteria:
- `python3 -m orders --version` prints `orders 1.0` and exits 0.

Notes: the requester calls it a tiny one that needs no interview.

## Deliveries

1. S1 alone.

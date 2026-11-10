# ADR-0001 — `count` reads the book through `load_orders`

**Status:** Accepted (2026-10-13)

## Context

`orders count` needs the number of orders in `data/orders.json`. It could read the file itself, or reuse `load_orders`, which `list` uses.

## Decision

`count` calls `load_orders()` and prints `len()` of the result. It relies on `load_orders` reading the file as the export tool writes it (A1).

Rejected: **its own JSON read**, a second place that knows the file's format.

## Consequences

- `count` fails exactly as `list` does on a malformed file.

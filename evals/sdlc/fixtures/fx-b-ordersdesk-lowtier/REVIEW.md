---
tiers:
  low: ["README.md", "docs/**"]
  medium: ["orders/**", "tests/**", "data/**"]
  high: [".github/**"]
---

# Review

What matters when reviewing a change to ordersdesk.

## What failure looks like

- An order is dropped, duplicated or reordered on its way out of `data/orders.json`.
- Money loses its two decimals, or a date stops being ISO.
- `orders list` output changes without the spec asking for it: accounting diffs it daily.

## Nits

At most three per review. Wording in README prose is a nit unless it is wrong.

## Skip

`data/orders.json` is sample data; do not review its contents.

## Evidence

Every finding names `file:line` and the input that breaks it.

## Summary

Lead with counts: findings by severity, then the findings.

## orders/**

Read `orders/store.py` before judging anything that loads orders: `load_orders` sorts oldest first.

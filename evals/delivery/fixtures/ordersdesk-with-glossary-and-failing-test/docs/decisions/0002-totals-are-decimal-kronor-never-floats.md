# 2. Totals are decimal kronor, never floats

Date: 2026-03-09

## Status

Accepted

## Context

Totals are money. Binary floats turn `89.50` into `89.5` and add rounding error when summed, and the accounting system rejects totals without two decimals.

## Decision

Totals are stored as strings with two decimals and loaded as `decimal.Decimal`. No code converts a total to `float`.

## Consequences

Every reader of the book keeps exact amounts. Anything that prints or writes a total formats it with two decimals itself.

# 1. Keep the order book in a JSON file

Date: 2026-03-02

## Status

Accepted

## Context

The back office has a few hundred orders a year and one person editing them. A database would need hosting and backups that nobody here looks after.

## Decision

The order book is one JSON file, `data/orders.json`, read whole by `orders.store.load_orders`. Nothing writes to it except a person with an editor.

## Consequences

The book is easy to inspect and diff. Concurrent edits are not supported, and the file is read in full on every command.

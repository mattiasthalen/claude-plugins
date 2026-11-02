# 1. The CSV export follows RFC 4180

Status: Accepted

## Context

`python3 -m orders export --csv <path>` writes every order for accounting's importer, which reads standard UTF-8 CSV with a header row. Customer names hold commas (`Berg, Hanna`) and non-ASCII letters (`Åkesson & Dotter`).

## Decision

The export writes RFC 4180 CSV through Python's `csv` module: comma-separated, fields quoted where they need it, UTF-8 without a byte-order mark, header `id,customer,total,placed_on`.

Joining fields by hand was rejected: `Berg, Hanna` would split into two columns.

## Consequences

The dialect is a contract with accounting's importer. Changing the delimiter, the quoting or the encoding needs their importer changed first.

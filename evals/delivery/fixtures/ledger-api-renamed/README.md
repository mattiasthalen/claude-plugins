# ledger-api

The Ledger service's customer records, served as JSON. The mobile app (`ledger-mobile`) is its main consumer.

```sh
python3 -m ledger_api customer C-1001   # print one customer record as JSON
python3 -m ledger_api customers         # print every customer record
python3 -m unittest discover -s tests
```

Design decisions are recorded in [docs/decisions/](docs/decisions/README.md).

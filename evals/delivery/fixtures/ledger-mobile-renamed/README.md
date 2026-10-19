# ledger-mobile

The Ledger mobile app's API client: it parses the customer records `ledger-api` serves into typed records the screens use.

```sh
python3 -m unittest discover -s tests
```

`tests/fixtures/customer.json` is a payload captured from the API. Design decisions are recorded in [docs/decisions/](docs/decisions/README.md).

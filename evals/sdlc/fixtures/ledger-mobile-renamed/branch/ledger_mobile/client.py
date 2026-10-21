"""Parses ledger-api payloads into the records the app's screens use."""
import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    account_id: str
    name: str
    currency: str

    def title(self):
        """The line shown at the top of the customer screen."""
        return f"{self.name} ({self.account_id})"


def parse_customer(payload):
    """A Customer from the API's JSON, given as text or as an already decoded dict."""
    data = json.loads(payload) if isinstance(payload, (str, bytes)) else payload
    # Payloads from before the rename carry only customerId (ledger-api ADR-0002).
    account_id = data["accountId"] if "accountId" in data else data["customerId"]
    return Customer(account_id=account_id, name=data["name"], currency=data["currency"])

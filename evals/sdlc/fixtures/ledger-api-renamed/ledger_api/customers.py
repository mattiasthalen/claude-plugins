"""Customer records, in the shape the API returns them (see docs/decisions/0001)."""
import json

_CUSTOMERS = {
    "C-1001": {"name": "Berg Konsult AB", "currency": "SEK"},
    "C-1002": {"name": "Nordvik Logistics", "currency": "NOK"},
    "C-1003": {"name": "Åkesson & Dotter", "currency": "SEK"},
}


class UnknownCustomer(KeyError):
    """No customer has the requested id."""


def get_customer(customer_id):
    """The record returned for GET /customers/<customer_id>."""
    try:
        record = _CUSTOMERS[customer_id]
    except KeyError:
        raise UnknownCustomer(customer_id) from None
    return {"customerId": customer_id, "name": record["name"], "currency": record["currency"]}


def list_customers():
    """Every customer record, ordered by id."""
    return [get_customer(customer_id) for customer_id in sorted(_CUSTOMERS)]


def to_json(payload):
    """Serialise a record or list of records exactly as the API sends it."""
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)

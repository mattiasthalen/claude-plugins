import unittest
from pathlib import Path

from ledger_mobile.client import Customer, parse_customer

SAMPLE = Path(__file__).parent / "fixtures" / "customer.json"


class ParseCustomerTest(unittest.TestCase):
    def test_parses_the_captured_api_payload(self):
        customer = parse_customer(SAMPLE.read_text(encoding="utf-8"))
        self.assertEqual(customer, Customer(customer_id="C-1001", name="Berg Konsult AB", currency="SEK"))

    def test_accepts_an_already_decoded_payload(self):
        customer = parse_customer({"customerId": "C-1003", "name": "Åkesson & Dotter", "currency": "SEK"})
        self.assertEqual(customer.customer_id, "C-1003")

    def test_title_shows_name_and_id(self):
        customer = parse_customer(SAMPLE.read_text(encoding="utf-8"))
        self.assertEqual(customer.title(), "Berg Konsult AB (C-1001)")


if __name__ == "__main__":
    unittest.main()

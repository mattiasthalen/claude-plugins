import unittest
from pathlib import Path

from ledger_mobile.client import Customer, parse_customer

SAMPLE = Path(__file__).parent / "fixtures" / "customer.json"


class ParseCustomerTest(unittest.TestCase):
    def test_parses_the_captured_api_payload(self):
        customer = parse_customer(SAMPLE.read_text(encoding="utf-8"))
        self.assertEqual(customer, Customer(account_id="C-1001", name="Berg Konsult AB", currency="SEK"))

    def test_accepts_an_already_decoded_payload(self):
        customer = parse_customer({"customerId": "C-1003", "name": "Åkesson & Dotter", "currency": "SEK"})
        self.assertEqual(customer.account_id, "C-1003")

    def test_title_shows_name_and_id(self):
        customer = parse_customer(SAMPLE.read_text(encoding="utf-8"))
        self.assertEqual(customer.title(), "Berg Konsult AB (C-1001)")



class RenameTest(unittest.TestCase):
    def test_parses_account_id(self):
        self.assertEqual(parse_customer({"accountId": "C-1", "name": "N", "currency": "SEK"}).account_id, "C-1")

    def test_parses_pre_rename_payload(self):
        self.assertEqual(parse_customer({"customerId": "C-1", "name": "N", "currency": "SEK"}).account_id, "C-1")

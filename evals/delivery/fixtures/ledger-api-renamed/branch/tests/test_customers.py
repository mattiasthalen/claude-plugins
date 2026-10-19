import json
import unittest

from ledger_api.customers import UnknownCustomer, get_customer, list_customers, to_json


class CustomerRecordTest(unittest.TestCase):
    def test_record_carries_customer_id_name_and_currency(self):
        self.assertEqual(
            get_customer("C-1001"),
            {"accountId": "C-1001", "customerId": "C-1001", "name": "Berg Konsult AB", "currency": "SEK"},
        )

    def test_unknown_customer_is_an_error(self):
        with self.assertRaises(UnknownCustomer):
            get_customer("C-9999")

    def test_records_are_listed_by_id(self):
        self.assertEqual([c["customerId"] for c in list_customers()], ["C-1001", "C-1002", "C-1003"])

    def test_json_keeps_non_ascii_names(self):
        payload = to_json(get_customer("C-1003"))
        self.assertIn("Åkesson & Dotter", payload)
        self.assertEqual(json.loads(payload)["customerId"], "C-1003")



class AccountIdTest(unittest.TestCase):
    def test_record_carries_account_id(self):
        self.assertEqual(get_customer("C-1001")["accountId"], "C-1001")

    def test_deprecated_customer_id_matches_account_id(self):
        record = get_customer("C-1002")
        self.assertEqual(record["customerId"], record["accountId"])

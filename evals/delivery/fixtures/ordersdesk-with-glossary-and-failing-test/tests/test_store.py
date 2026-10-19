import json
import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from orders.store import load_orders


class LoadOrdersTest(unittest.TestCase):
    def test_orders_are_sorted_oldest_first(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "orders.json"
            path.write_text(json.dumps([
                {"id": 2, "customer": "B", "total": "5.00", "placed_on": "2026-03-02"},
                {"id": 1, "customer": "A", "total": "7.50", "placed_on": "2026-03-01"},
            ]))
            orders = load_orders(path)
        self.assertEqual([o.id for o in orders], [1, 2])
        self.assertEqual(orders[0].total, Decimal("7.50"))
        self.assertEqual(orders[0].placed_on, date(2026, 3, 1))

    def test_the_book_has_six_customers(self):
        customers = {o.customer for o in load_orders()}
        self.assertEqual(len(customers), 6)


if __name__ == "__main__":
    unittest.main()

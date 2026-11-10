import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from orders.__main__ import main
from orders.store import load_orders


def run(argv, book):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "orders.json"
        path.write_text(json.dumps(book))
        out = io.StringIO()
        with mock.patch("orders.__main__.load_orders", lambda: load_orders(path)), contextlib.redirect_stdout(out):
            code = main(argv)
        return code, out.getvalue()


BOOK = [{"id": 1, "customer": "A", "total": "7.50", "placed_on": "2026-03-01"},
        {"id": 2, "customer": "B", "total": "5.00", "placed_on": "2026-03-02"}]


class CountTest(unittest.TestCase):
    def test_ac1_prints_number_of_orders(self):
        self.assertEqual(run(["count"], BOOK), (0, "2\n"))

    def test_ac2_empty_book_prints_zero(self):
        self.assertEqual(run(["count"], []), (0, "0\n"))

    def test_ac3_list_unchanged(self):
        code, out = run(["list"], BOOK)
        self.assertEqual(code, 0)
        self.assertEqual(len(out.splitlines()), 2)


if __name__ == "__main__":
    unittest.main()

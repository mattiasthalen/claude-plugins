import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def export(*args):
    return subprocess.run([sys.executable, "-m", "orders", "export", *args], cwd=ROOT, capture_output=True, text=True)


class ExportTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "out.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def rows(self):
        with open(self.path, encoding="utf-8", newline="") as f:
            return list(csv.reader(f))

    def test_writes_header_and_every_order_in_list_order(self):
        self.assertEqual(export("--csv", str(self.path)).returncode, 0)
        rows = self.rows()
        self.assertEqual(rows[0], ["id", "customer", "total", "placed_on"])
        self.assertEqual([r[0] for r in rows[1:]], ["1001", "1002", "1003", "1004", "1005"])

    def test_comma_stays_one_field_and_non_ascii_survives(self):
        export("--csv", str(self.path))
        customers = [r[1] for r in self.rows()[1:]]
        self.assertIn("Berg, Hanna", customers)
        self.assertIn("Åkesson & Dotter", customers)
        self.assertFalse(self.path.read_bytes().startswith(b"\xef\xbb\xbf"))

    def test_totals_keep_two_decimals_and_dates_are_iso(self):
        export("--csv", str(self.path))
        row = self.rows()[2]
        self.assertEqual(row[2:], ["89.50", "2026-09-03"])

    def test_missing_csv_is_a_usage_error(self):
        result = export()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("usage", result.stderr)


if __name__ == "__main__":
    unittest.main()

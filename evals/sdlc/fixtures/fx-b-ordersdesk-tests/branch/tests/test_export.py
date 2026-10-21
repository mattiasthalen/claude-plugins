"""Checks for the CSV export, one per criterion of the approved spec (C1-C5, E1-E2)."""
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

    def test_c1_exits_zero_and_writes_the_header(self):
        self.assertEqual(export("--csv", str(self.path)).returncode, 0)
        self.assertEqual(self.path.read_text(encoding="utf-8").splitlines()[0], "id,customer,total,placed_on")

    def test_c2_every_order_once_in_list_order(self):
        export("--csv", str(self.path))
        self.assertEqual([r[0] for r in self.rows()[1:]], ["1001", "1002", "1003", "1004", "1005"])

    def test_c3_comma_is_quoted_and_stays_one_field(self):
        export("--csv", str(self.path))
        self.assertIn('"Berg, Hanna"', self.path.read_text(encoding="utf-8"))
        row = next(r for r in self.rows()[1:] if r[0] == "1004")
        self.assertEqual(row, ["1004", "Berg, Hanna", "15.00", "2026-09-08"])

    def test_c4_utf8_without_bom(self):
        export("--csv", str(self.path))
        self.assertFalse(self.path.read_bytes().startswith(b"\xef\xbb\xbf"))
        self.assertIn("Åkesson & Dotter", [r[1] for r in self.rows()[1:]])

    def test_c5_two_decimals_and_iso_dates(self):
        export("--csv", str(self.path))
        rows = {r[0]: r for r in self.rows()[1:]}
        self.assertEqual(rows["1002"][2:], ["89.50", "2026-09-03"])
        self.assertEqual(rows["1004"][2], "15.00")

    def test_e1_missing_csv_is_a_usage_error(self):
        result = export()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("usage", result.stderr)
        self.assertIn("--csv", result.stderr)

    def test_e2_unwritable_path_reports_the_os_error(self):
        result = export("--csv", str(Path(self.tmp.name) / "missing" / "out.csv"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("No such file or directory", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()

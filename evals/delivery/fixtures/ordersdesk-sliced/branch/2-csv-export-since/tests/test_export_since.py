import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def export(*args):
    return subprocess.run([sys.executable, "-m", "orders", "export", *args], cwd=ROOT, capture_output=True, text=True)


class ExportSinceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "out.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def ids(self):
        with open(self.path, encoding="utf-8", newline="") as f:
            return [r[0] for r in list(csv.reader(f))[1:]]

    def test_since_keeps_only_later_orders(self):
        self.assertEqual(export("--csv", str(self.path), "--since", "2026-09-08").returncode, 0)
        self.assertEqual(self.ids(), ["1004", "1005"])

    def test_since_includes_the_day_itself(self):
        export("--csv", str(self.path), "--since", "2026-09-03")
        self.assertEqual(self.ids(), ["1002", "1003", "1004", "1005"])

    def test_bad_since_is_a_usage_error(self):
        result = export("--csv", str(self.path), "--since", "3/9")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid fromisoformat value", result.stderr)


if __name__ == "__main__":
    unittest.main()

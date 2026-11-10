import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent / "vendor.sh"


class VendorUsage(unittest.TestCase):
    def setUp(self):
        # A PATH holding only what the usage path needs, so a gh or jq call fails the test.
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for tool in ("bash", "sed", "dirname"):
            Path(tmp.name, tool).symlink_to(shutil.which(tool))
        self.env = {"PATH": tmp.name}

    def run_script(self, *args):
        return subprocess.run(
            [shutil.which("bash"), str(SCRIPT), *args], env=self.env, capture_output=True, text=True
        )

    def assert_help(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertRegex(result.stdout, r"(?m)^#\s+vendor\.sh .*--help")
        self.assertIn("vendor.sh --refresh", result.stdout)
        self.assertIn("Copies are changed only here", result.stdout)

    def assert_misuse(self, result):
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, self.run_script("--help").stdout)

    def test_long_help_prints_usage_to_stdout(self):
        self.assert_help(self.run_script("--help"))

    def test_short_help_matches_long_help(self):
        self.assertEqual(self.run_script("-h").stdout, self.run_script("--help").stdout)
        self.assert_help(self.run_script("-h"))

    def test_help_ignores_later_arguments(self):
        self.assert_help(self.run_script("--help", "--check"))

    def test_no_argument_is_misuse(self):
        self.assert_misuse(self.run_script())

    def test_unknown_flag_is_misuse(self):
        self.assert_misuse(self.run_script("--bogus"))

    def test_help_is_case_sensitive(self):
        self.assert_misuse(self.run_script("--HELP"))

    def test_ci_runs_these_tests(self):
        workflow = (SCRIPT.parent.parent / ".github" / "workflows" / "validate.yml").read_text()
        self.assertIn("unittest discover -s scripts -p 'test_*.py'", workflow)


if __name__ == "__main__":
    unittest.main()

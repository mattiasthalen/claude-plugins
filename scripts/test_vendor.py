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
        self.assertRegex(result.stdout, r"vendor\.sh .*--help")
        self.assertIn("vendor.sh --refresh", result.stdout)
        self.assertIn("Copies are changed only here", result.stdout)

    def assert_misuse(self, result):
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, self.run_script("--help").stdout)

    def test_long_help_prints_usage_to_stdout(self):
        self.assert_help(self.run_script("--help"))

    def test_short_help_matches_long_help(self):
        short = self.run_script("-h")
        self.assertEqual(short.stdout, self.run_script("--help").stdout)
        self.assert_help(short)

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


# BSD and macOS sed refuse a command followed directly by "}" ("extra characters at the end
# of p command", compile.c in Apple's text_cmds), and CI runs only GNU sed, which accepts it.
STRICT_SED = """#!{bash}
for arg in "$@"; do
  case "$arg" in *[!\\;]}}*) echo "sed: extra characters at the end of p command" >&2; exit 1;; esac
done
exec {sed} "$@"
"""


class VendorUsageUnderBsdSed(VendorUsage):
    def setUp(self):
        super().setUp()
        sed = Path(self.env["PATH"], "sed")
        sed.unlink()
        sed.write_text(STRICT_SED.format(bash=shutil.which("bash"), sed=shutil.which("sed")))
        sed.chmod(0o755)


if __name__ == "__main__":
    unittest.main()

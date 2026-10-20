"""ablate.py's verdicts on incomplete results.

    python3 evals/delivery/tools/test_ablate.py

A unit marked earned stays in the skill, so a result that cannot judge a unit must ask for a
rerun rather than read as a drop.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ablate  # noqa: E402


def write_result(runs, partial=False):
    path = Path(tempfile.mkdtemp()) / "result.json"
    path.write_text(json.dumps({"partial": partial, "cases": [{"name": "s1-x", "arms": {"with": runs}}]}))
    return path


def run(*graders, error=None):
    return {"error": error, "graders": [dict(g) for g in graders]}


PASS = {"name": "shape-a", "passed": True}
FAIL = {"name": "shape-a", "passed": False}


class BelowBar(unittest.TestCase):
    def test_missing_result_asks_for_a_rerun(self):
        self.assertIsNone(ablate.below_bar([Path(tempfile.mkdtemp()) / "none.json"], 5))

    def test_errored_run_asks_for_a_rerun(self):
        self.assertIsNone(ablate.below_bar([write_result([run(PASS)] * 4 + [run(error="session limit")])], 5))

    def test_fewer_runs_than_asked_asks_for_a_rerun(self):
        self.assertIsNone(ablate.below_bar([write_result([run(PASS)] * 3)], 5))

    def test_partial_result_asks_for_a_rerun(self):
        self.assertIsNone(ablate.below_bar([write_result([run(PASS)] * 5, partial=True)], 5))

    def test_unscored_grader_is_not_a_drop(self):
        unscored = {"name": "content-a", "passed": False, "scored": False}
        self.assertEqual(ablate.below_bar([write_result([run(PASS, unscored)] * 5)], 5), [])

    def test_shape_grader_failing_once_is_a_drop(self):
        self.assertEqual(ablate.below_bar([write_result([run(PASS)] * 4 + [run(FAIL)])], 5), ["s1-x/shape-a"])


if __name__ == "__main__":
    unittest.main()

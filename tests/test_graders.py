"""Shape graders checked offline against trace lines of the form the eval runner records.

A tool call reaches a grader as `"name":"Edit","input":{...}`, and Claude Code writes Edit's input with
`replace_all` before `file_path`, so a pattern that expects `file_path` first never sees an Edit.
"""
import importlib.util
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("gen", REPO / "evals/sdlc/gen.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


def call(name, **tool_input):
    return json.dumps({"type": "tool_use", "id": "toolu_1", "name": name, "input": tool_input}, separators=(",", ":"))


def grader(case, name):
    return gen.CASE_SPECS[case]["graders"][name]


def matches(g, line):
    return re.search(g.get("pattern") or g["input_match"], line) is not None


class WriteGraderTest(unittest.TestCase):
    def test_nothing_in_repo_catches_an_edit_outside_the_scratchpad(self):
        g = grader("intent-stories", "shape-nothing-in-repo")
        self.assertTrue(matches(g, call("Edit", replace_all=False, file_path="/w/cwd/README.md", old_string="a", new_string="b")))
        self.assertTrue(matches(g, call("Write", file_path="/w/cwd/docs/stories.md", content="x")))
        self.assertFalse(matches(g, call("Write", file_path="/w/cwd/.scratchpad/sdlc/x/stories.md", content="x")))

    def test_no_source_write_catches_edits_under_orders_and_tests(self):
        g = gen.NO_SOURCE_WRITE
        self.assertTrue(matches(g, call("Edit", replace_all=False, file_path="/w/cwd/orders/__main__.py", old_string="a", new_string="b")))
        self.assertFalse(matches(g, call("Write", file_path="/w/cwd/.scratchpad/sdlc/orders-count/stories.md", content="x")))


class SkillGraderTest(unittest.TestCase):
    def test_intent_grader_ignores_intent_in_another_skills_arguments(self):
        g = grader("flow-kickoff", "shape-intent")
        self.assertTrue(matches(g, json.dumps({"skill": "sdlc:intent"})))
        self.assertFalse(matches(g, json.dumps({"skill": "design:design-interview", "args": "the intent of S1"})))

    def test_kickoff_grades_that_the_flow_loads(self):
        self.assertIn("shape-flow", gen.CASE_SPECS["flow-kickoff"]["graders"])


class GenerateTest(unittest.TestCase):
    def test_a_missing_plugin_stops_generation(self):
        run = subprocess.run([sys.executable, str(REPO / "evals/sdlc/gen.py")], env={"SDLC_PLUGIN": "plugins/nope", "PATH": "/usr/bin:/bin"},
                             capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)


if __name__ == "__main__":
    unittest.main()

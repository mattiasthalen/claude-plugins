"""Shape graders checked offline against trace lines of the form the eval runner records.

A tool call reaches a grader as `"name":"Edit","input":{...}`, and Claude Code writes Edit's input with
`replace_all` before `file_path`, so a pattern that expects `file_path` first never sees an Edit.
"""
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("gen", REPO / "evals/sdlc/gen.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


JS_CHECK = """
const checks = JSON.parse(require("fs").readFileSync(0, "utf8"));
process.stdout.write(JSON.stringify(checks.map(([pattern, flags, line]) => {
  let u_error = null;
  try { new RegExp(pattern, "u"); } catch (e) { u_error = e.message; }
  return {u_error, matched: new RegExp(pattern, flags).test(line)};
})));
"""


def js_check(checks):
    """For each (pattern, flags, line): the error compiling the pattern under `u`, or None, and whether the pattern,
    compiled with the flags the eval runner gives it (a regex grader's own, none for an input_match), matches the line."""
    node = shutil.which("node")
    if node is None:
        raise RuntimeError("node is not on PATH: grader patterns are checked in the JavaScript engine the eval runner uses")
    run = subprocess.run([node, "-e", JS_CHECK], input=json.dumps(checks), capture_output=True, text=True, check=True)
    return json.loads(run.stdout)


def call(name, **tool_input):
    return json.dumps({"type": "tool_use", "id": "toolu_1", "name": name, "input": tool_input}, separators=(",", ":"))


def tool_input(**fields):
    """A tool_used grader's input_match is tested against the tool's input, compact as JSON.stringify writes it."""
    return json.dumps(fields, separators=(",", ":"))


def skill(name, **args):
    return tool_input(skill=name, **args)


def bash(command):
    return tool_input(command=command)


# Per grader pattern: a line it must match, then a line it must not.
SAMPLES = {
    r'"skill":\s*"(?:code-review|simplify)"': (skill("simplify"), skill("implementation:code-review")),
    r'"skill":\s*"design:design-interview"': (skill("design:design-interview"), skill("design:adr", args="design:design-interview")),
    r'"skill":\s*"design:design-philosophy"': (skill("design:design-philosophy"), skill("design:design-interview")),
    r'"skill":\s*"implementation:code-style"': (skill("implementation:code-style"), skill("code-style")),
    r'"skill":\s*"implementation:review-cycle"': (skill("implementation:review-cycle"), skill("code-review")),
    gen.HIJACK: (skill("mattpocock-skills:tdd"), skill("mattpocock-skills:pr")),
    r'"skill":\s*"mattpocock-skills:pr"': (skill("mattpocock-skills:pr"), skill("mattpocock-skills:prototype")),
    r'"skill":\s*"sdlc:intent"': (skill("sdlc:intent"), skill("design:design-interview", args="the intent of S1")),
    r'"skill":\s*"sdlc:sdlc"': (skill("sdlc:sdlc"), skill("sdlc:intent")),
    r'\.scratchpad/sdlc/[^"]+/stories\.md': (tool_input(file_path="/w/cwd/.scratchpad/sdlc/packed/stories.md", content="x"),
                                             tool_input(file_path="/w/cwd/docs/stories.md", content="x")),
    r"\bgh ": (bash("gh issue create --title S2"), bash("echo high ")),
    "gh issue create": (bash("gh issue create --title S2"), bash("gh issue list")),
    "gh pr create": (bash("gh pr create --fill"), bash("gh pr view 7")),
    "git push": (bash("git push -u origin main"), bash("git commit -m push")),
    gen.no_write(r'(?![^"]*\.scratchpad/)')["pattern"]: (
        call("Edit", replace_all=False, file_path="/w/cwd/README.md", old_string="a", new_string="b"),
        call("Write", file_path="/w/cwd/.scratchpad/sdlc/packed/stories.md", content="x")),
    gen.NO_SOURCE_WRITE["pattern"]: (
        call("Edit", replace_all=False, file_path="/w/cwd/orders/__main__.py", old_string="a", new_string="b"),
        call("Write", file_path="/w/cwd/.scratchpad/sdlc/orders-count/stories.md", content="x")),
    gen.no_write(r'[^"]*/tests/')["pattern"]: (call("Write", file_path="/w/cwd/tests/test_count.py", content="x"),
                                              call("Write", file_path="/w/cwd/orders/__main__.py", content="x")),
    gen.no_write(r'[^"]*stories\.md"')["pattern"]: (call("Write", file_path="/w/cwd/.scratchpad/sdlc/x/stories.md", content="x"),
                                                    call("Write", file_path="/w/cwd/.scratchpad/sdlc/x/intent.md", content="x")),
}


def grader(case, name):
    return gen.CASE_SPECS[case]["graders"][name]


def matches(g, line):
    [result] = js_check([(g.get("pattern") or g["input_match"], g.get("flags", ""), line)])
    return result["matched"]


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


def suite_patterns():
    """Every pattern a non-judge grader in the suite matches with, and the flags the eval runner compiles it with."""
    found = set()
    for spec in gen.CASE_SPECS.values():
        for g in spec["graders"].values():
            if g["type"] != "llm":
                found.add((g.get("pattern") or g["input_match"], g.get("flags", "")))
    return found


class PatternCoverageTest(unittest.TestCase):
    def test_every_pattern_compiles_under_the_u_flag(self):
        patterns = sorted(suite_patterns())
        results = js_check([(p, flags, "") for p, flags in patterns])
        invalid = {p: r["u_error"] for (p, _), r in zip(patterns, results) if r["u_error"]}
        self.assertEqual(invalid, {})

    def test_every_pattern_matches_its_sample_and_not_its_counter_sample(self):
        checks, expected = [], []
        for p, flags in sorted(suite_patterns()):
            if p in SAMPLES:
                must_match, must_not_match = SAMPLES[p]
                checks += [(p, flags, must_match), (p, flags, must_not_match)]
                expected += [True, False]
        wrong = [f"{'missed' if want else 'matched'} {line!r} with {p!r}"
                 for (p, _, line), want, r in zip(checks, expected, js_check(checks)) if r["matched"] != want]
        self.assertEqual(wrong, [])

    def test_every_pattern_has_samples_and_every_sample_a_pattern(self):
        in_suite = {p for p, _ in suite_patterns()}
        self.assertEqual(sorted(in_suite - SAMPLES.keys()), [], "patterns without a sample pair")
        self.assertEqual(sorted(SAMPLES.keys() - in_suite), [], "samples for a pattern no grader uses")

    def test_the_u_check_catches_an_escape_that_python_and_plain_js_accept(self):
        re.compile(r"\'")
        [result] = js_check([(r"\'", "", "'")])
        self.assertTrue(result["u_error"])
        self.assertTrue(result["matched"])

    def test_a_tool_used_grader_without_input_match_has_no_pattern_to_check(self):
        specs = {"any-case": {"graders": {"shape-wrote": gen.grader("tool_used", tool="Write")}}}
        with mock.patch.dict(gen.CASE_SPECS, specs, clear=True):
            self.assertEqual(suite_patterns(), set())

    def test_without_node_the_check_fails_rather_than_skips(self):
        with mock.patch.dict(os.environ, {"PATH": ""}):
            with self.assertRaises(RuntimeError):
                js_check([("a", "", "a")])


class GenerateTest(unittest.TestCase):
    def test_a_missing_plugin_stops_generation(self):
        run = subprocess.run([sys.executable, str(REPO / "evals/sdlc/gen.py")], env={"SDLC_PLUGIN": "plugins/nope", "PATH": "/usr/bin:/bin"},
                             capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)


if __name__ == "__main__":
    unittest.main()

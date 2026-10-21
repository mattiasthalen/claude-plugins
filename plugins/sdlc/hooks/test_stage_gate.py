import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import stage_gate  # noqa: E402

HOOK = Path(__file__).with_name("stage_gate.py")


class Run:
    def __init__(self, phase, scratchpad=True):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.repo = root / "repo"
        self.repo.mkdir()
        self.env = {"TMPDIR": str(root / "tmp")}
        self.event = {"session_id": "s1", "cwd": str(self.repo), "tool_name": "Write"}
        if scratchpad:
            self.event["scratchpad_dir"] = str(root / "scratch")
        self.docs = stage_gate.docs_dir(self.event, self.env)
        if phase:
            self.docs.mkdir(parents=True)
            (self.docs / "phase").write_text(phase + "\n")

    def decide(self, path, agent=None, **extra):
        event = dict(self.event, tool_input={"file_path": path}, **extra)
        if agent:
            event["agent_type"] = agent
        return stage_gate.decide(event, self.env)


class StageGate(unittest.TestCase):
    def run_in(self, phase, scratchpad=True):
        r = Run(phase, scratchpad)
        self.addCleanup(r.tmp.cleanup)
        return r

    def test_inert_without_phase(self):
        r = self.run_in(None)
        self.assertIsNone(r.decide("src/app.py"))
        self.assertIsNone(r.decide("tests/test_app.py"))

    def test_inert_when_done(self):
        r = self.run_in("done")
        self.assertIsNone(r.decide("tests/test_app.py"))

    def test_pre_approval_only_docs(self):
        for phase in ("spec", "plan"):
            r = self.run_in(phase)
            self.assertIsNotNone(r.decide("src/app.py"))
            self.assertIsNotNone(r.decide("tests/test_app.py", agent=stage_gate.TEST_WRITER))
            self.assertIsNone(r.decide(str(r.docs / "spec.md")))

    def test_test_stage_only_tests_by_writer(self):
        r = self.run_in("test")
        self.assertIsNone(r.decide("tests/test_app.py", agent=stage_gate.TEST_WRITER))
        self.assertIsNotNone(r.decide("tests/test_app.py"))
        self.assertIsNotNone(r.decide("src/app.py", agent=stage_gate.TEST_WRITER))
        self.assertIsNone(r.decide(str(r.docs / "plan.md")))

    def test_build_blocks_tests_outside_writer(self):
        for phase in ("build", "review", "prove", "ship"):
            r = self.run_in(phase)
            self.assertIsNone(r.decide("src/app.py"))
            self.assertIsNotNone(r.decide("tests/test_app.py"))
            self.assertIsNotNone(r.decide("evals/sdlc/s1/graders/shape-x.md"))
            self.assertIsNone(r.decide("tests/test_app.py", agent=stage_gate.TEST_WRITER))

    def test_test_file_shapes(self):
        cwd = "/r"
        for p in ("/r/tests/a.py", "/r/pkg/test_a.py", "/r/a_test.go", "/r/web/a.test.ts", "/r/a.spec.js",
                  "/r/web/__tests__/x.js", "/r/evals/x/prompt.md", "/r/conftest.py"):
            self.assertTrue(stage_gate.is_test_file(p, cwd), p)
        for p in ("/r/src/app.py", "/r/docs/testing.md", "/r/latest.py"):
            self.assertFalse(stage_gate.is_test_file(p, cwd), p)

    def test_without_scratchpad_uses_tmpdir_per_session(self):
        r = self.run_in("plan", scratchpad=False)
        self.assertEqual(r.docs, Path(r.env["TMPDIR"]) / "sdlc-s1")
        self.assertIsNotNone(r.decide("src/app.py"))

    def test_sessions_do_not_share_phase(self):
        r = self.run_in("plan", scratchpad=False)
        other = dict(r.event, session_id="s2", tool_input={"file_path": "src/app.py"})
        self.assertIsNone(stage_gate.decide(other, r.env))

    def test_notebook_path(self):
        r = self.run_in("build")
        event = dict(r.event, tool_name="NotebookEdit", tool_input={"notebook_path": "tests/nb_test.ipynb"})
        self.assertIsNotNone(stage_gate.decide(event, r.env))

    def test_exit_code_and_stderr(self):
        r = self.run_in("plan")
        event = dict(r.event, tool_input={"file_path": "src/app.py"})
        p = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(event), text=True, capture_output=True,
                           env=dict(os.environ, **r.env))
        self.assertEqual(p.returncode, 2)
        self.assertIn("before the plan is approved", p.stderr)
        event["tool_input"] = {"file_path": str(r.docs / "plan.md")}
        p = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(event), text=True, capture_output=True,
                           env=dict(os.environ, **r.env))
        self.assertEqual(p.returncode, 0)


if __name__ == "__main__":
    unittest.main()

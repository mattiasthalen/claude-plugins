#!/usr/bin/env python3
"""PreToolUse gate on file writes during an sdlc run (ADR-0009).

The run's phase lives in `<docs>/phase`, where <docs> is `<scratchpad>/sdlc`, or
`$TMPDIR/sdlc-<session_id>` (the Bash tool's $TMPDIR) in a session without a scratchpad. The skill writes the
phase as each stage starts; with no phase file, or phase `done`, the gate is inert.

    spec, plan   writes only into <docs>
    test         <docs>, and test files from the test-writer agent
    build, review, prove, ship
                 anything, except test files outside the test-writer agent

Exit 2 refuses the call; stderr is what the agent reads.
"""
import fnmatch
import json
import os
import sys
from pathlib import Path

TEST_WRITER = "sdlc:test-writer"
# A file name (case-insensitive), a CamelCase test class file (FooTest.java, FooTests.cs), or any
# directory on the path below the repository root (case-insensitive).
TEST_NAMES = ("test_*", "*_test.*", "*.test.*", "*.spec.*", "*_spec.*", "conftest.py")
CAMEL_TEST_NAMES = ("*Test.*", "*Tests.*")
TEST_DIRS = {"tests", "test", "__tests__", "spec", "testdata", "evals"}
PRE_APPROVAL = {"spec", "plan"}
POST_TEST = {"build", "review", "prove", "ship"}


def docs_dir(event, env=os.environ):
    """The run's folder. Without a scratchpad it is under the Bash tool's $TMPDIR, which a sandboxed
    session nests as <TMPDIR>/claude-<uid> below the TMPDIR this hook sees: the candidate holding a
    phase file wins."""
    if event.get("scratchpad_dir"):
        return Path(event["scratchpad_dir"]) / "sdlc"
    tmp = Path(env.get("TMPDIR") or "/tmp")
    name = f"sdlc-{event.get('session_id', '')}"
    dirs = [tmp / name, tmp / f"claude-{os.getuid()}" / name]
    return next((d for d in dirs if (d / "phase").is_file()), dirs[0])


def repo_root(path, cwd):
    """The nearest directory above path holding .git, else cwd: a `cd tests` must not hide a test."""
    for d in Path(path).resolve().parents:
        if (d / ".git").exists():
            return d
    return Path(cwd).resolve()


def is_test_file(path, cwd):
    p = Path(path).resolve()
    try:
        parts = p.relative_to(repo_root(p, cwd)).parts
    except ValueError:
        parts = p.parts
    name = parts[-1]
    return any(fnmatch.fnmatch(name.lower(), g) for g in TEST_NAMES) or any(
        fnmatch.fnmatchcase(name, g) for g in CAMEL_TEST_NAMES) or any(
        d.lower() in TEST_DIRS or d.lower().endswith((".tests", ".test")) for d in parts[:-1])


def inside(path, root):
    try:
        Path(path).resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def decide(event, env=os.environ):
    """None to allow, or the refusal message."""
    docs = docs_dir(event, env)
    try:
        phase = (docs / "phase").read_text(encoding="utf-8").strip()
    except OSError:
        return None
    if phase not in PRE_APPROVAL | {"test"} | POST_TEST:
        return None
    tool_input = event.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not path:
        return None
    cwd = event.get("cwd") or os.getcwd()
    path = str(Path(cwd, path)) if not os.path.isabs(path) else path
    if inside(path, docs):
        return None
    writer = event.get("agent_type") == TEST_WRITER
    test = is_test_file(path, cwd)
    if phase in PRE_APPROVAL:
        return (f"sdlc {phase} stage: nothing is written outside {docs} before the plan is approved. "
                f"Write the {phase} document there. If no sdlc run is going on, write done to {docs}/phase.")
    if phase == "test":
        if test and writer:
            return None
        if test:
            return f"sdlc test stage: tests are written by the {TEST_WRITER} agent. Dispatch it with the spec and plan."
        return "sdlc test stage: only tests are written now. The build starts after the test gate."
    if test and not writer:
        return (f"sdlc {phase} stage: tests are fixed at the test gate. If a check is wrong, stop: report it at the "
                f"evidence gate for a re-plan. A regression test review proved missing goes to {TEST_WRITER}.")
    return None


def main():
    event = json.load(sys.stdin)
    message = decide(event)
    if message:
        print(message, file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()

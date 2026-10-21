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
TEST_GLOBS = (
    "test_*", "*_test.*", "*.test.*", "*.spec.*", "conftest.py",
    "tests/*", "test/*", "__tests__/*", "spec/*", "evals/*",
)
PRE_APPROVAL = {"spec", "plan"}
POST_TEST = {"build", "review", "prove", "ship"}


def docs_dirs(event, env=os.environ):
    """Where the run's folder can be. Without a scratchpad it is under the Bash tool's $TMPDIR, which a
    sandboxed session nests as <TMPDIR>/claude-<uid> below the TMPDIR this hook sees."""
    if event.get("scratchpad_dir"):
        return [Path(event["scratchpad_dir"]) / "sdlc"]
    tmp = Path(env.get("TMPDIR", "/tmp"))
    name = f"sdlc-{event.get('session_id', '')}"
    return [tmp / name, tmp / f"claude-{os.getuid()}" / name]


def docs_dir(event, env=os.environ):
    """The run's folder: the first candidate holding a phase file, else the first candidate."""
    dirs = docs_dirs(event, env)
    return next((d for d in dirs if (d / "phase").is_file()), dirs[0])


def is_test_file(path, cwd):
    p = Path(path)
    try:
        rel = p.resolve().relative_to(Path(cwd).resolve())
    except ValueError:
        rel = p
    parts = rel.parts
    if any(fnmatch.fnmatch(parts[-1], g) for g in TEST_GLOBS if "/" not in g):
        return True
    dirs = {g.split("/")[0] for g in TEST_GLOBS if "/" in g}
    return any(d in dirs for d in parts[:-1])


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
                f"Write the {phase} document there.")
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

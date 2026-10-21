#!/usr/bin/env python3
"""PreToolUse hook: refuse Claude's edits to vendored copies (ADR-0013).

Vendored directories are the `dest` entries of scripts/vendor.json; only
scripts/vendor.sh changes them. VENDORED.md in each is ours and stays editable.
"""
import json
import os
import sys
from pathlib import Path


def vendored(root):
    manifest = Path(root) / "scripts" / "vendor.json"
    try:
        return [Path(root, e["dest"]) for e in json.loads(manifest.read_text())["copies"]]
    except (OSError, KeyError, ValueError):
        return []


def decide(event, root):
    tool_input = event.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not path:
        return None
    p = Path(event.get("cwd") or root, path).resolve()
    if p.name == "VENDORED.md":
        return None
    for d in vendored(root):
        try:
            p.relative_to(d.resolve())
        except ValueError:
            continue
        return f"{d.relative_to(root)} is a vendored copy: refresh it with scripts/vendor.sh, never by hand."
    return None


def main():
    event = json.load(sys.stdin)
    message = decide(event, os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or os.getcwd())
    if message:
        print(message, file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()

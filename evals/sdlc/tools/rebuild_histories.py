#!/usr/bin/env python3
"""Rebuild every staged case's history.jsonl from its conversation.md and the current skill.

    python3 evals/sdlc/tools/rebuild_histories.py           # after every edit to the skill
    python3 evals/sdlc/tools/rebuild_histories.py --check   # exit 1 if any history is stale (CI)

A history embeds the skill's body where the conversation invokes /sdlc, so
it goes stale whenever plugins/sdlc/skills/sdlc/SKILL.md changes.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
COMPOSE = Path(__file__).with_name("compose_history.py")
check = "--check" in sys.argv


def project_cwd(scaffold):
    """/work/<project>: the first fixture the stage's scaffold copies, or for a multi-repo spec
    (fixture:dir) the fixture's family (ledger-api-renamed:api → ledger)."""
    first = scaffold.read_text(encoding="utf-8").split('scaffold.sh"', 1)[1].split()[0]
    return "/work/" + (first.split("-")[0] if ":" in first else first)


stale = []
for conversation in sorted(ROOT.glob("evals/sdlc/*/*/conversation.md")):
    history = conversation.with_name("history.jsonl")
    old = history.read_text(encoding="utf-8") if history.exists() else ""
    cwd = project_cwd(conversation.with_name("scaffold.sh"))
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "history.jsonl"
        subprocess.run([sys.executable, str(COMPOSE), str(conversation), str(out), "--cwd", cwd], check=True)
        new = out.read_text(encoding="utf-8")
    if new != old:
        stale.append(str(history.relative_to(ROOT)))
        if not check:
            history.write_text(new, encoding="utf-8")
print(("stale: " if check else "rebuilt: ") + str(len(stale)))
for s in stale:
    print("  ", s)
sys.exit(1 if check and stale else 0)

#!/usr/bin/env python3
"""Compose a resumable conversation for a staged case.

    python3 evals/sdlc/tools/compose_history.py <conversation.md> <history.jsonl> [--cwd /work/<project>]

A staged case resumes a conversation through `context.history_file`, and its prompt is the
next user turn. The conversation is written as markdown, one turn per section:

    ## user
    /sdlc Add CSV export of orders.

    ## assistant
    A few questions before I plan this ...

Only `## user` and `## assistant` headings start a turn; everything up to the next one is the
turn's text, verbatim. The runner needs nothing more than user and assistant records chained by
uuid and parentUuid, so that is all this writes. Identifiers and timestamps are derived from the
turn's position, which keeps the output byte-identical across rebuilds.

A user turn that invokes `/sdlc` (or `/sdlc:sdlc`) is written the way Claude Code records a real
invocation: the command, then a meta record carrying the skill's current body. Without it a
resumed stage would never see the skill, and lines earned for it would have no effect there.
The body is read from plugins/sdlc/skills/sdlc/SKILL.md at build time, so a history goes stale
whenever the skill changes: rebuild them all with evals/sdlc/tools/rebuild_histories.py.
"""
from pathlib import Path
import json
import re
import sys

args = sys.argv[1:]
if len(args) < 2:
    sys.exit(__doc__)
src, out = args[0], args[1]
cwd = args[args.index("--cwd") + 1] if "--cwd" in args else "/work/project"

turns, role, lines = [], None, []
for line in open(src, encoding="utf-8").read().splitlines():
    m = re.fullmatch(r"## (user|assistant)\s*", line)
    if m:
        if role:
            turns.append((role, "\n".join(lines).strip("\n")))
        role, lines = m.group(1), []
    elif role:
        lines.append(line)
if role:
    turns.append((role, "\n".join(lines).strip("\n")))
if not turns or turns[0][0] != "user":
    sys.exit(f"{src}: a conversation starts with a '## user' turn")
for i in range(1, len(turns)):
    if turns[i][0] == turns[i - 1][0]:
        sys.exit(f"{src}: turn {i + 1} repeats the role '{turns[i][0]}'; turns must alternate")

SESSION = "00000000-0000-4000-8000-0000000000aa"
SKILL = Path(__file__).resolve().parents[3] / "plugins" / "sdlc" / "skills" / "sdlc" / "SKILL.md"
INVOKE = re.compile(r"/(?:sdlc:)?sdlc(?:\s+(.*))?\Z", re.S)


def skill_body():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"---\n.*?\n---\n?(.*)", text, re.S)
    return (m.group(1) if m else text).strip("\n")


records = []
for role, text in turns:
    m = INVOKE.match(text) if role == "user" else None
    if not m:
        records.append((role, text, {}))
        continue
    args = (m.group(1) or "").strip()
    records.append(("user", "<command-message>sdlc:sdlc</command-message>\n"
                    "<command-name>/sdlc:sdlc</command-name>\n"
                    f"<command-args>{args}</command-args>", {}))
    meta = f"Base directory for this skill: /work/plugin/skills/sdlc\n\n{skill_body()}\n\nARGUMENTS: {args}"
    records.append(("user", [{"type": "text", "text": meta}], {"isMeta": True}))
parent = None
with open(out, "w", encoding="utf-8") as f:
    for i, (role, text, extra) in enumerate(records):
        uid = f"00000000-0000-4000-8000-{i:012d}"
        stamp = f"2026-10-13T09:{i // 60:02d}:{i % 60:02d}.000Z"
        if role == "user":
            message = {"role": "user", "content": text}
        else:
            message = {"model": "claude-opus-5-5", "id": f"msg_{i:024d}", "type": "message", "role": "assistant",
                       "content": [{"type": "text", "text": text}], "stop_reason": "end_turn",
                       "stop_sequence": None, "usage": {"input_tokens": 0, "output_tokens": 0}}
        record = {"type": role, "isSidechain": False, "sessionId": SESSION, "version": "2.1.287", "cwd": cwd,
                  "userType": "external", "timestamp": stamp, "message": message, "uuid": uid, "parentUuid": parent, **extra}
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
        parent = uid

#!/usr/bin/env python3
"""Test every regex shape grader against its sample texts, offline.

    python3 evals/sdlc/tools/test_shape_graders.py [evals-dir]

A regex grader that false-fails a correct run is the worst outcome when lines are earned by evals: the skill
would grow a line to satisfy a pattern. So every `shape-*` regex grader has samples that must
pass and samples that must fail, in its scenario's grader-samples.md:

    ### plan/graders/shape-brief-has-guardrails.md
    Must pass:
    ```
    **Guardrails**
    ```
    Must fail:
    ```
    No constraints listed.
    ```

A sample is read as a file is: its text ends with a newline. Patterns are JavaScript regular expressions, run here with Python's `re`. The two agree on
everything the suite uses (classes, groups, alternation, `[\\s\\S]`, lazy quantifiers); a grader
that needs JavaScript-only syntax fails here, on purpose. Python's `re` is the looser of the two
on escapes: it reads `\\'` or `\\;` as the bare character, while the harness compiles with the `u`
flag, which rejects an identity escape and then reports "pattern not found" (a `contains` grader
fails, a `not_contains` grader passes vacuously). So every pattern is also compiled with
`new RegExp(pattern, 'u')` under `node`, when `node` is on PATH; without it that check is skipped
and says so. Exits non-zero when any sample disagrees with its grader, a regex shape grader has
no samples, or a pattern does not compile under either engine.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "evals/sdlc")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    fields = {}
    for line in (m.group(1) if m else "").splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
                v = v[1:-1].replace("''", "'") if v[0] == "'" else v[1:-1].encode().decode("unicode_escape")
            fields[k.strip()] = v
    return fields


def samples(md):
    found = {}
    for section in re.split(r"^### ", md.read_text(encoding="utf-8"), flags=re.M)[1:]:
        name, body = section.split("\n", 1)
        parts = re.split(r"^Must (pass|fail):\s*$", body, flags=re.M)
        entry = {"pass": [], "fail": []}
        for kind, chunk in zip(parts[1::2], parts[2::2]):
            entry[kind] += [t + "\n" for t in re.findall(r"```[^\n]*\n(.*?)\n```", chunk, re.S)]
        found[name.strip()] = entry
    return found


failures, checked = [], 0
# A tool_used grader with max but no min expects at least one call: "never" must say min: 0.
for g in sorted(root.glob("*/*/graders/shape-*.md")):
    fm = frontmatter(g)
    if fm.get("type") == "tool_used" and "max" in fm and "min" not in fm:
        failures.append(f"{g.relative_to(root)}: max without min means at least one call; add min: 0")
for scenario in sorted(p for p in root.iterdir() if p.is_dir()):
    graders = sorted(scenario.glob("*/graders/shape-*.md"))
    regexes = [g for g in graders if frontmatter(g).get("type") == "regex"]
    if not regexes:
        continue
    md = scenario / "grader-samples.md"
    known = samples(md) if md.exists() else {}
    for g in regexes:
        key = str(g.relative_to(scenario))
        fm = frontmatter(g)
        flags = re.I if "i" in fm.get("flags", "") else 0
        flags |= re.M if "m" in fm.get("flags", "") else 0
        flags |= re.S if "s" in fm.get("flags", "") else 0
        negate = fm.get("match") == "not_contains"
        try:
            pattern = re.compile(fm["pattern"], flags)
        except re.error as e:
            failures.append(f"{scenario.name}/{key}: pattern does not compile: {e}")
            continue
        entry = known.get(key)
        if not entry or not entry["pass"] or not entry["fail"]:
            failures.append(f"{scenario.name}/{key}: needs at least one 'Must pass' and one 'Must fail' sample")
            continue
        for kind in ("pass", "fail"):
            for text in entry[kind]:
                checked += 1
                passed = bool(pattern.search(text)) != negate
                if passed != (kind == "pass"):
                    failures.append(f"{scenario.name}/{key}: a must-{kind} sample {'failed' if kind == 'pass' else 'passed'}: {text[:80]!r}")

# Mirrors the harness's compile, `u` plus the grader's own flags.
JS_COMPILE = """
const graders = JSON.parse(require("fs").readFileSync(0, "utf8"));
for (const [name, pattern, flags] of graders) {
  try { new RegExp(pattern, "u" + flags.replace(/[^ims]/g, "")); }
  catch (e) { console.log(name + ": pattern does not compile under JavaScript's u flag: " + e.message.split(": ").pop()); }
}
"""
regex_graders = [
    (f"{g.parent.parent.parent.name}/{g.relative_to(g.parent.parent.parent)}", fm["pattern"], fm.get("flags", ""))
    for g in sorted(root.glob("*/*/graders/shape-*.md"))
    for fm in [frontmatter(g)]
    if fm.get("type") == "regex" and "pattern" in fm
]
node = shutil.which("node")
if node:
    out = subprocess.run([node, "-e", JS_COMPILE], input=json.dumps(regex_graders), text=True, capture_output=True, check=True)
    failures += out.stdout.splitlines()
    print(f"{len(regex_graders)} patterns compiled under JavaScript's u flag")
else:
    print(f"skip: node is not on PATH, so {len(regex_graders)} patterns were not compiled under JavaScript's u flag")

for f in failures:
    print("✘", f)
print(f"{checked} samples checked, {len(failures)} problems")
sys.exit(1 if failures else 0)

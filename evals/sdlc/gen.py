"""Writes the sdlc eval cases into evals/sdlc/cases/, which git ignores.

Each case starts at one step of the flow on the ordersdesk fixture (lib/scaffold.sh), with the
conversation so far as a seeded history and the requester's next line as its prompt. A history
records a skill load the way Claude Code does, with the skill's current body, so re-run this after
every change to a SKILL.md, or after fetch-deps.sh picks up a new upstream version.
"""
import json
import os
import re
import shutil
from pathlib import Path

SUITE = Path(__file__).resolve().parent
REPO = SUITE.parent.parent
CASES = SUITE / "cases"
# A copy of the plugin with one line taken out, to show the line is earned: its case goes red without it.
SDLC = os.environ.get("SDLC_PLUGIN", "plugins/sdlc")
SKILLS = {
    "sdlc:sdlc": REPO / SDLC / "skills/sdlc/SKILL.md",
    "sdlc:intent": REPO / SDLC / "skills/intent/SKILL.md",
    "design:design-interview": REPO / ".eval-deps/design/skills/design-interview/SKILL.md",
}
PLUGINS = [SDLC, ".eval-deps/design", ".eval-deps/implementation", ".eval-deps/mattpocock-skills"]
# The eval runner names no scratchpad, so each case names one inside the workspace, git-ignored by the scaffold.
SCRATCHPAD = ("Scratchpad directory: `.scratchpad/` in the working directory. Git ignores it. Use it for working "
              "documents and temporary files instead of /tmp.")
TOOLS = ["Read", "Glob", "Grep", "Bash", "Write", "Edit", "Skill", "Agent", "TaskCreate", "TaskUpdate", "TaskList", "TaskGet"]

ASK = "Add an `orders count` command that prints how many orders there are."
VAGUE = "I'd like ordersdesk to be more useful for the warehouse team."
STORIES_SHOWN = ("Here are the stories, in `.scratchpad/sdlc/orders-count/stories.md`:\n\n"
    "- **S1. Count the orders** (now). [stated] `orders count` prints the number of orders and nothing else. "
    "[proposed] An empty book prints 0, since that is the first edge a clerk meets.\n"
    "- **S2. Count by customer** (later).\n\nNon-goal: `orders list` stays as it is. What's wrong or missing?")
FILING_ASKED = "Approved. Should any of these go on a tracker, S2 for example, or stay in the stories file only?"
DESIGNED = ("The design interview is done: every branch is closed, with 0 gaps. No fork was ADR-worthy, and the lexicon "
    "and assumptions record are unchanged. The brief is in `.scratchpad/sdlc/orders-count/` next to `stories.md`: "
    "`functional-spec.md`, `edge-cases.md` and `acceptance-criteria.md` (AC1 prints the count, AC2 an empty book "
    "prints 0, AC3 `list` unchanged). Next is tests first. Shall I go on?")
BUILT_GREEN = ("Tests first: `tests/test_count.py` covers AC1 to AC3, and all three were red and committed before any "
    "code. Built: a `count` subcommand in `orders/__main__.py`; all 4 tests are green.")
BUILT = BUILT_GREEN + " Next is the review."
REVIEWED = (BUILT_GREEN + " Review cycle ran (adversarial, design parity, simplification): "
    "1) the README does not mention `count`, listed as a follow-up; 2) no test for a malformed data file, rejected "
    "because edge-cases.md puts it out of scope. No existing test changed.")
PROOF = ("The proof is up: AC1 to AC3 going red to green, the full local suite at head (4 OK), both review findings "
    "with their outcomes, and no change to an existing test. Waiting for your go before I open the PR.")
CAPTURED = ("The design interview is done: every branch is closed, with 0 gaps. Capture wrote the brief to "
    "`.scratchpad/sdlc/orders-count/` next to `stories.md` (`functional-spec.md`, `edge-cases.md`, "
    "`acceptance-criteria.md`: AC1 prints the count, AC2 an empty book prints 0, AC3 `list` unchanged), and committed "
    "ADR-0001, ADR-0002 and the assumptions record on `feat/orders-count`. Every [stated] criterion is covered. Shall I go on?")
PR_OPEN = "PR is open: https://github.com/example/ordersdesk/pull/7, `Add an orders count command`."

INTERVIEW = [
    ("user", "Approved. Don't file anything."),
    ("skill", "design:design-interview", "Pitch: S1, `orders count` prints the number of orders and nothing else "
        "(stated); an empty book prints 0 (proposed). Non-goal: `orders list` stays as it is. S2, count by customer, "
        "is later and out of scope."),
    ("assistant", "Scope as I read it: a `count` subcommand beside `list`, printing a bare integer; `list` and the "
        "data file stay untouched; S2 is out. Assumption: the book fits in memory, as `list` already loads it whole. "
        "Is that right?"),
    ("user", "Correct."),
    ("assistant", "First branch, the interface: does `count` take any flags or filters, or is it exactly "
        "`orders count` with no arguments?"),
    ("user", "No flags."),
    ("assistant", "Recap: `orders count` takes no arguments and prints one integer and a newline, exit 0. "
        "What case would break this?"),
]

HIJACK = (r'"skill":\s*"mattpocock-skills:(?:tdd|grilling|grill-me|grill-with-docs|codebase-design|domain-modeling|'
          r'to-spec|implement|implement-spec|code-review)"')


def grader(kind, **fields):
    return {"type": kind, **fields}


def skill_used(pattern, **limits):
    return grader("tool_used", tool="Skill", input_match=pattern, **limits)


def skill_named(name, **limits):
    return skill_used(rf'"skill":\s*"{name}"', **limits)


def no_write(path_pattern):
    """No Write or Edit whose file_path matches; Edit's input carries replace_all before file_path."""
    return grader("regex", target="trace", match="not_contains",
                  pattern=r'"name":\s*"(?:Write|Edit)",\s*"input":\s*\{[^}]*"file_path":\s*"' + path_pattern)


def judge(focus, body):
    return grader("llm", focus=focus, body=body)


NO_HIJACK = skill_used(HIJACK, min=0, max=0)
NO_SOURCE_WRITE = no_write(r'[^"]*/(?:orders|tests)/')
NO_DESIGN = skill_named("design:design-interview", min=0, max=0)
NO_FILING = grader("tool_used", tool="Bash", input_match=r"gh issue create", min=0, max=0)

CASE_SPECS = {
    "flow-kickoff": dict(
        desc="A change request with no size word starts with intent and stops on one question.",
        state="base", history=[], prompt=ASK, turns=40, timeout=900, graders={
            "shape-flow": skill_named("sdlc:sdlc"),
            "shape-intent": skill_named("sdlc:intent"),
            "shape-no-code": NO_SOURCE_WRITE,
            "content-one-question": judge("last_message",
                "Judge one thing only: does the reply end waiting on the requester, on a question about the "
                "`orders count` change (why it is wanted, who it is for, what it must do), without asking whether "
                "the change is small, and without reporting any code or tests written?\n\nPASS if all of that holds.\n\n"
                "FAIL if it asks whether the change is small or can skip a step, writes or reports code or tests, or "
                "ends without a question to the requester."),
        }),
    "flow-small": dict(
        desc="The requester calls the change small: no intent, no design, a test before any code.",
        state="base", history=[], prompt="Small change: add an `orders count` command that prints how many orders there are.",
        turns=60, timeout=1500, graders={
            "shape-no-intent": skill_named("sdlc:intent", min=0, max=0),
            "shape-no-design": NO_DESIGN,
            "content-test-first": judge("trace",
                "Judge one thing only: before the first Write or Edit to a file under `orders/`, did the run write "
                "a test for the new `count` command and run it? A failed git commit is expected in this sandbox and "
                "not held against the run.\n\nPASS if a test for `count` is written and run before any change under "
                "`orders/`, or the run stops after the tests without touching `orders/`.\n\nFAIL if `orders/` changes "
                "first, no test for `count` is written, or the run asks whether to skip tests."),
        }),
    "flow-tests-first": dict(
        desc="Design approved: a test per criterion, red and committed before code.",
        state="designed", history=[("user", ASK), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"),
                                   ("assistant", STORIES_SHOWN), *INTERVIEW[:1], ("assistant", DESIGNED)],
        prompt="Looks good, go ahead.", turns=80, timeout=1800, graders={
            "shape-philosophy": skill_named("design:design-philosophy"),
            "shape-code-style": skill_named("implementation:code-style"),
            "content-red-committed-first": judge("trace",
                "Judge one thing only: before any Write or Edit to a file under `orders/`, did the run write a test "
                "for each of AC1, AC2 and AC3, run them and see the new behaviour fail, and attempt `git commit` of "
                "those tests? The sandbox makes the git directory read-only, so the commit itself fails; that is "
                "expected. AC3 (`list` unchanged) cannot start red, so stopping before the commit to flag that to the "
                "requester also counts.\n\nPASS if tests for every AC are written and run before the first change under "
                "`orders/`, and the run either attempts a commit of them or stops to flag the criterion that cannot start "
                "red (stopping after the failed commit is fine).\n\nFAIL if code "
                "under `orders/` changes before that, the tests are not run, no commit is attempted, or the run builds "
                "anyway after the failed commit."),
        }),
    "flow-coverage": dict(
        desc="The brief misses a stated story criterion: the gap goes to the requester before any test.",
        state="designed-gap", history=[("user", ASK), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"),
                                       ("assistant", STORIES_SHOWN), *INTERVIEW[:1], ("assistant", DESIGNED)],
        prompt="Looks good, go ahead.", turns=60, timeout=1500, graders={
            "shape-no-test-written": no_write(r'[^"]*/tests/'),
            "content-gap-reported": judge("last_message",
                "Judge one thing only: S1 in `stories.md` has a [stated] criterion about `orders count --since "
                "2026-09-03`, and no acceptance criterion in the brief covers it. Does the reply tell the requester "
                "about that uncovered criterion and wait for their call?\n\nPASS if it names the `--since` criterion "
                "(or S1's date filter) as not covered by the brief and asks how to proceed.\n\nFAIL if it does not "
                "mention it, or mentions it only after writing tests."),
        }),
    "flow-platform-docs": dict(
        desc="Capture committed a platform assumption only the documentation settles: review-cycle catches it before any test.",
        state="captured", history=[("user", ASK), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"),
                                   ("assistant", STORIES_SHOWN), *INTERVIEW[:1], ("assistant", CAPTURED)],
        prompt="Looks good, go ahead.", turns=60, timeout=1800, graders={
            "shape-review-cycle": skill_named("implementation:review-cycle"),
            "content-cron-caught": judge("trace",
                "Judge one thing only: assumption A2 in `docs/assumptions.md` (and ADR-0002) says GitHub Actions "
                "`schedule` cron runs in the repository owner's time zone. It does not: scheduled workflows run in UTC "
                "unless a `timezone` is set. Before the first Write or Edit to a file under `tests/` or `orders/`, does the "
                "run find that A2 is wrong and say so to the requester (or stop to report it)?\n\nPASS if the run "
                "reports A2 or the cron hour as wrong before any such write.\n\nFAIL if a test or code file is written "
                "first, or A2 is never questioned."),
        }),
    "flow-review": dict(
        desc="Build green: review runs through implementation:review-cycle, not a built-in reviewer.",
        state="built", history=[("user", ASK), ("load", "sdlc:sdlc"), ("assistant", DESIGNED),
                                ("user", "Looks good, go ahead."), ("assistant", BUILT)],
        prompt="Carry on.", turns=80, timeout=1800, graders={
            "shape-review-cycle": skill_named("implementation:review-cycle"),
            "shape-no-builtin-review": skill_used(r'"skill":\s*"(?:code-review|simplify)"', min=0, max=0),
        }),
    "flow-go-gate": dict(
        desc="Review done: show the proof and stop for the go; no PR.",
        state="built", history=[("user", ASK), ("load", "sdlc:sdlc"), ("assistant", DESIGNED),
                                ("user", "Looks good, go ahead."), ("assistant", REVIEWED)],
        prompt="Great, carry on.", turns=60, timeout=1500, graders={
            "shape-no-pr-skill": skill_named("mattpocock-skills:pr", min=0, max=0),
            "shape-no-gh-pr": grader("tool_used", tool="Bash", input_match="gh pr create", min=0, max=0),
            "shape-no-push": grader("tool_used", tool="Bash", input_match="git push", min=0, max=0),
            "content-proof-and-wait": judge("last_message",
                "Judge one thing only: does the reply present the proof (each acceptance criterion's red-to-green "
                "result, the full local suite at head, each review finding and its outcome, and any change to an "
                "existing test, whether as a published page, a written file, or inline because publishing was "
                "unavailable) and then wait for the requester's go before any pull request?\n\nPASS if it shows that "
                "proof and asks for the go.\n\nFAIL if it opens or says it is opening a pull request, or ends without "
                "asking for the go."),
        }),
    "flow-pr-on-go": dict(
        desc="Go given: open the PR with mattpocock-skills:pr.",
        state="built", history=[("user", ASK), ("load", "sdlc:sdlc"), ("assistant", DESIGNED),
                                ("user", "Looks good, go ahead."), ("assistant", REVIEWED),
                                ("user", "Great, carry on."), ("assistant", PROOF)],
        prompt="Go.", turns=40, timeout=900, graders={
            "shape-pr-skill": skill_named("mattpocock-skills:pr"),
        }),
    "flow-retro": dict(
        desc="Merged: remind the requester to run the retro.",
        state="built", history=[("user", ASK), ("load", "sdlc:sdlc"), ("assistant", REVIEWED),
                                ("user", "Great, carry on."), ("assistant", PROOF), ("user", "Go."), ("assistant", PR_OPEN)],
        prompt="Merged.", turns=20, timeout=600, graders={
            "content-retro-reminder": judge("last_message",
                "Judge one thing only: does the reply remind the requester to run `/mattpocock-skills:retro` (by "
                "that name)?\n\nPASS if it does.\n\nFAIL if it does not name the retro skill."),
        }),
    "flow-mid-interview": dict(
        desc="Two steps into the design interview with Pocock fully loaded: no Pocock skill, one next question.",
        state="base", history=[("user", ASK), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"),
                               ("assistant", STORIES_SHOWN), *INTERVIEW],
        prompt="Nothing breaks it, close it.", turns=30, timeout=900, graders={
            "shape-no-code": NO_SOURCE_WRITE,
            "content-next-question": judge("last_message",
                "Judge one thing only: does the reply close the interface branch and carry the design interview on "
                "by asking the requester the next design question?\n\nPASS if it does, whether one question or a short "
                "batch of related ones.\n\nFAIL if it starts writing code or tests, ends the interview with branches "
                "still open, or asks nothing."),
        }),
    "flow-no-trigger": dict(
        desc="A question that changes nothing in the repo loads neither the flow nor intent.",
        state="base", history=[], prompt="What does `orders/store.py` do? Just explain it.", turns=10, timeout=300,
        graders={"shape-no-flow": skill_named("sdlc:sdlc", min=0, max=0),
                 "shape-no-intent": skill_named("sdlc:intent", min=0, max=0)}),
    "intent-why-first": dict(
        desc="A vague idea gets one open question about the why, before any story.",
        state="base", history=[], prompt=VAGUE, turns=30, timeout=900, graders={
            "shape-intent": skill_named("sdlc:intent"),
            "shape-no-stories": no_write(r'[^"]*stories\.md"'),
            "content-open-why": judge("last_message",
                "Judge one thing only: does the reply ask the requester an open question about why they want this "
                "or what problem the warehouse team has, without offering a list of options or features to pick "
                "from?\n\nPASS if it ends on one such open question, a single question.\n\nFAIL if it proposes options, features or "
                "stories, asks only a closed or multiple-choice question, or asks nothing."),
        }),
    "intent-stories": dict(
        desc="The why is answered: stories go to the scratchpad with marked criteria and dispositions.",
        state="base", history=[("user", VAGUE), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"),
                               ("assistant", "Before anything: what is the warehouse team struggling with today?")],
        prompt=("They pick orders from `orders list` and lose track of which ones are already packed. They want to "
                "mark an order packed and list only the unpacked ones. Don't touch totals or invoicing. That's all I "
                "know; write it up."), turns=40, timeout=900, graders={
            "shape-stories-in-scratchpad": grader("tool_used", tool="Write", input_match=r'\.scratchpad/sdlc/[^"]+/stories\.md'),
            "shape-nothing-in-repo": no_write(r'(?![^"]*\.scratchpad/)'),
            "content-marks-and-dispositions": judge("trace",
                "Judge one thing only: in the content written to `stories.md`, does every acceptance criterion carry "
                "a [stated] or [proposed] mark, and does every story carry a disposition of now, later or drop, in any form (a `Disposition:` line, or a label beside the story's title)?\n\n"
                "PASS if both hold for every criterion and story in the last version written.\n\nFAIL if any "
                "criterion lacks a mark, any story lacks a disposition, or no stories.md was written."),
        }),
    "intent-filing-ask": dict(
        desc="Stories approved: intent asks whether to file any, and files nothing yet.",
        state="designed", history=[("user", ASK), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"), ("assistant", STORIES_SHOWN)],
        prompt="Looks right. Approved.", turns=20, timeout=600, graders={
            "shape-no-design-yet": NO_DESIGN,
            "shape-no-filing": NO_FILING,
            "content-asks-to-file": judge("last_message",
                "Judge one thing only: does the reply ask the requester whether any of the stories should be filed on "
                "a tracker, and wait for the answer?\n\nPASS if it asks that and waits.\n\nFAIL if it files, says it "
                "will file, or moves on without asking."),
        }),
    "intent-filing-no": dict(
        desc="Filing declined: nothing filed, and the hand-off pitch carries the non-goal and the later story.",
        state="designed", history=[("user", ASK), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"), ("assistant", STORIES_SHOWN),
                                   ("user", "Looks right. Approved."), ("assistant", FILING_ASKED)],
        prompt="No, don't file anything.", turns=30, timeout=900, graders={
            "shape-design": skill_named("design:design-interview"),
            "shape-no-filing": NO_FILING,
            "content-handoff-pitch": judge("trace",
                "Judge one thing only: the run calls the Skill tool for `design:design-interview`. Do that call's "
                "arguments, or the message that introduces the interview, carry S1's criteria, the non-goal that "
                "`orders list` stays as it is, and S2 named as out of scope?\n\nPASS if all three are there.\n\nFAIL "
                "if any is missing or design-interview is never called."),
        }),
    "intent-filing-fails": dict(
        desc="A filing fails: the failure is reported, naming the story, before design starts.",
        state="designed", history=[("user", ASK), ("load", "sdlc:sdlc"), ("load", "sdlc:intent"), ("assistant", STORIES_SHOWN),
                                   ("user", "Looks right. Approved."), ("assistant", FILING_ASKED)],
        prompt="File S2 as a GitHub issue in this repo, then carry on.", turns=30, timeout=900, graders={
            "shape-filing-tried": grader("tool_used", tool="Bash", input_match=r"\bgh "),
            "content-failure-reported": judge("trace",
                "Judge one thing only: filing S2 fails in this sandbox. Does the run tell the requester that filing S2 "
                "failed, and why, in a message before any Skill call to design-interview (or with no such call)?\n\n"
                "PASS if it does.\n\nFAIL if it moves on to design without reporting the failure, or claims S2 was filed."),
        }),
}
for spec in CASE_SPECS.values():
    spec["graders"].setdefault("shape-no-hijack", NO_HIJACK)


def skill_body(name):
    path = SKILLS[name]
    if not path.exists():
        raise SystemExit(f"gen.py: {path} is missing; run evals/fetch-deps.sh, or check SDLC_PLUGIN")
    return re.sub(r"\A---\n.*?\n---\n", "", path.read_text(), flags=re.S).strip()


def records(history):
    """Turns a case's history into (role, content, extra) records."""
    out = []
    for i, step in enumerate(history):
        kind = step[0]
        if kind in ("load", "skill"):
            name, args = step[1], step[2] if len(step) > 2 else None
            body = skill_body(name)
            tool_id = f"toolu_{i:026d}"
            call = {"skill": name, **({"args": args} if args else {})}
            out += [("assistant", [{"type": "tool_use", "id": tool_id, "name": "Skill", "input": call}], {}),
                    ("user", [{"type": "tool_result", "tool_use_id": tool_id, "content": f"Launching skill: {name}"}], {}),
                    ("user", [{"type": "text", "text": f"Base directory for this skill: /plugins/{name}\n\n{body}"}], {"isMeta": True})]
        else:
            out.append((kind, step[1], {}))
    return out


def write_history(path, history):
    session = "00000000-0000-4000-8000-0000000000aa"
    parent = None
    with open(path, "w") as f:
        for i, (role, content, extra) in enumerate(records(history)):
            uid = f"00000000-0000-4000-8000-{i:012d}"
            if role == "user":
                message = {"role": "user", "content": content}
            else:
                blocks = content if isinstance(content, list) else [{"type": "text", "text": content}]
                message = {"model": "claude-opus-5-5", "id": f"msg_{i:024d}", "type": "message", "role": "assistant",
                           "content": blocks, "stop_reason": "tool_use" if isinstance(content, list) else "end_turn",
                           "stop_sequence": None, "usage": {"input_tokens": 0, "output_tokens": 0}}
            f.write(json.dumps({"type": role, "isSidechain": False, "sessionId": session, "version": "2.1.322",
                                "cwd": "/work/project", "userType": "external", "timestamp": f"2026-11-10T09:00:{i:02d}.000Z",
                                "message": message, "uuid": uid, "parentUuid": parent, **extra}) + "\n")
            parent = uid


def front_matter(fields):
    return "---\n" + "".join(f"{k}: {json.dumps(v)}\n" for k, v in fields.items()) + "---\n"


def write_case(name, spec):
    case = CASES / name
    (case / "graders").mkdir(parents=True)
    fields = {"description": spec["desc"], "plugins": [f"../../../../{p}" for p in PLUGINS], "max_turns": spec["turns"],
              "timeout_seconds": spec["timeout"], "runs": 3, "allowed_tools": TOOLS, "append_system_prompt": SCRATCHPAD}
    (case / "prompt.md").write_text(front_matter(fields) + "\n" + spec["prompt"] + "\n")
    context = "  scaffold_script: scaffold.sh\n" + ("  history_file: history.jsonl\n" if spec["history"] else "")
    (case / "case.yaml").write_text(f'schema_version: "1.1"\nname: {name}\ncontext:\n{context}')
    (case / "scaffold.sh").write_text('#!/usr/bin/env bash\nset -euo pipefail\n'
                                      f'bash "$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)/../../lib/scaffold.sh" {spec["state"]}\n')
    if spec["history"]:
        write_history(case / "history.jsonl", spec["history"])
    for grader_name, g in spec["graders"].items():
        g = dict(g)
        body = g.pop("body", "")
        (case / "graders" / f"{grader_name}.md").write_text(front_matter(g) + (f"\n{body}\n" if body else ""))


if __name__ == "__main__":
    shutil.rmtree(CASES, ignore_errors=True)
    for name, spec in CASE_SPECS.items():
        write_case(name, spec)
    print("\n".join(sorted(CASE_SPECS)))

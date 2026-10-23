# Grader samples — Spec publishing

Offline samples for every regex shape grader in this scenario; `python3 evals/sdlc/tools/test_shape_graders.py` checks them. The `tool_used` graders' `input_match` patterns are not checked by it; their samples are kept here as documentation:

- `shape-no-gh-issue` `\bgh\s+(?:issue\b|api\b[^\n]*\bissues\b)` (max 0) matches `{"command": "gh issue create --title x"}` and `{"command": "gh issue view 7"}`; it does not match `{"command": "gh auth status"}`.
- `shape-no-gh-issue-write` `\bgh\s+(?:issue\s+(?:create|edit|comment|close|reopen)\b|api\b[^\n]*\bissues\b)` (max 0) matches `{"command": "gh issue edit 8 --body-file x.md"}`, `{"command": "gh issue comment 8 --body \"Amended: C6\""}` and `{"command": "gh api -X PATCH repos/example/ordersdesk/issues/8 -f body=x"}`; it does not match `{"command": "gh issue view 8"}` or `{"command": "gh auth status"}`.

`shape-issue-body-no-run-path` is a regex grader over the whole trace (`not_contains`): a run-folder path (`sdlc-<id>/`, `/sdlc/`, `sdlc-handoff/`) must not be text in the issue's body, whether the body is inline in the `gh issue create` command, fed on stdin (a pipe or heredoc into `--body-file -`), or in a file a Write or Bash call wrote earlier and the `gh issue create` reads by `--body-file`/`-F` under the same file name. A path used as a file is not text: the operand of `cat`, `--body-file`/`-F`, or a `<`/`>` redirect passes, so `cat sdlc-handoff/spec.md | gh issue create --body-file -` and `--body-file "$TMPDIR/sdlc-3f2a/issue.md"` are fine; only what such a file holds is checked. Inside a `$(…)`, each command is judged on its own: one that starts with `cat`, `sed`, `head` or `tail` reads its operands as files, while a path in any other (`echo`, `printf`) is body text, so `--body "$(cat sdlc-handoff/spec.md; printf '\nRefs #7\n')"` passes and `--body "$(cat sdlc-handoff/spec.md; echo Full spec: /tmp/sdlc-ab/spec.md)"` fails. An `echo` or `printf` counts only at a command start (the command's start, or after `;`, `&`, `|`, `(`, `{`, a newline, `then`, `else` or `do`), so a long command is scanned once rather than again from every `echo` word in it.

`shape-issue-body-is-spec` is a regex grader over the whole trace, not a judged one: a judge of a long resumed run sees only the trace's head and tail (about 23 KB), and the filing call sits in between. It matches the compact tool call as `trace.jsonl` writes it (`"name":"Bash","input":{"command":"…"}`), its body inline in that command, or in a file a Write or Bash call wrote earlier and the `gh issue create` reads by `--body-file`/`-F` under the same file name. For the spec, a body is also the spec when the command feeds a `spec.md` file to `gh` (`cat` into the `--body-file`, a pipe into `--body-file -`, `--body "$(cat …)"`, `--body-file …/spec.md`, `< …/spec.md`); such a body needs no `#7` in the command, because the fixture's spec names `issue #7` itself. An inline or written body must hold the C1 and C5 rows and `#7`.

`shape-one-gh-issue-create` is a regex grader over the whole trace, not a `tool_used` count: a count also took Bash calls the harness refused before running them (a `<tool_use_error>`, such as `allowed_domains cannot widen network access`) and calls where `gh` never ran (a `> "$TMPDIR/…" && gh issue create …` whose redirect failed with `Read-only file system`), so a run that filed once was failed for its retries. It pairs each `gh issue create` Bash call (`"id":"toolu_…","name":"Bash","input":{"command":"…"`) with its `tool_result` by `tool_use_id`, in either key order, and counts the call as a filing attempt when the result is not a `<tool_use_error>` or a `Permission to use` refusal, and either shows `gh` ran (`api.github.com`, an issue URL, `gh auth login`, `GH_TOKEN`, `GraphQL:`, `HTTP 4xx/5xx`, `could not add label`) or carries no shell error (`bash: line N: `, `zsh:N: `, `sh: `) other than the harness's own `…/cwd-…: ` file. Anchored at the trace's start, it passes when such an attempt exists and no second one with another id does. `shape-no-gh-issue-create` and `shape-no-gh-issue` stay `tool_used` counts: there a refused call is still an attempt to file.

### docs-say/graders/shape-issue-body-no-run-path.md
Must pass:
```
"name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } | gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file -","description":"File the approved spec as a GitHub issue linked to #7"}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body \"$(cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n')\""}
```
Must pass:
```
"name":"Bash","input":{"command":"cat sdlc-handoff/spec.md > \"$TMPDIR/sdlc-3f2a/issue.md\" && printf '\\nRefs #7\\n' >> \"$TMPDIR/sdlc-3f2a/issue.md\" && gh issue create --title Spec --label spec -F \"$TMPDIR/sdlc-3f2a/issue.md\" 2>&1"}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec: CSV export\" --label spec --body-file - < \"$TMPDIR/sdlc-3f2a/spec.md\""}
```
Must pass:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/issue.md","content":"# Spec — CSV export of all orders\n\n| C1 | every order, one row each |\n| C5 | header row first |\n\nRefs #7\n"}
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/issue.md\""}
```
Must pass:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/notes.md","content":"copied from sdlc-handoff/spec.md"}
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/issue.md\""}
```
Must pass:
```
"name":"Bash","input":{"command":"cp sdlc-handoff/spec.md \"$TMPDIR/sdlc-3f2a/body.md\" && printf '\\nRefs #7\\n' >> \"$TMPDIR/sdlc-3f2a/body.md\" && gh issue create --title Spec --label spec -F \"$TMPDIR/sdlc-3f2a/body.md\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body-file=/tmp/sdlc-ab/issue.md"}
```
Must pass:
```
"name":"Bash","input":{"command":"{ printf 'Refs #7\\n\\n'; sed -e 's|`intent.md` in this run.s folder|story #7|' sdlc-handoff/spec.md; } | gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file -","description":"File the approved spec as a GitHub issue linked to #7"}
```
Must pass:
```
"name":"Bash","input":{"command":"head -n 400 /tmp/sdlc-ab/spec.md | gh issue create --title Spec --label spec --body-file -"}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body-file sdlc-handoff/spec.md 2>&1 | tee \"$TMPDIR/sdlc-3f2a/gh.log\""}
```
Must pass:
```
"name":"Bash","input":{"command":"BODY=/tmp/sdlc-ab/issue.md; gh issue create --title Spec --label spec --body-file \"$BODY\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body-file sdlc-handoff/spec.md; echo \"log in $TMPDIR/sdlc-3f2a/gh.log\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"$(sed -e '1d' sdlc-handoff/spec.md)\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body \"See $TMPDIR/sdlc-3f2a/spec.md. Refs #7\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"Spec at sdlc-handoff/spec.md\""}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/issue.md","content":"# Spec — CSV export of all orders\n\n| C1 | every order, one row each |\n| C5 | header row first |\n\nRefs #7\n\nFull spec: /tmp/sdlc-ab/spec.md\n"}
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/issue.md\""}
```
Must fail:
```
"name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nFull spec: /tmp/sdlc-ab/spec.md\\nRefs #7\\n'; } > \"$TMPDIR/body.md\""}
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec -F \"$TMPDIR/body.md\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body-file - <<'EOF'\n# Spec\n| C1 | every order |\nRefs #7\nFull spec: /tmp/sdlc-ab/spec.md\nEOF"}
```
Must fail:
```
"name":"Bash","input":{"command":"printf 'Full spec: %s\\n' \"$TMPDIR/sdlc-3f2a/spec.md\" | gh issue create --title Spec --label spec --body-file -"}
```

Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec -b 'Full spec: /tmp/sdlc-ab/spec.md'"}
```
Must fail:
```
"name":"Bash","input":{"command":"cat <<'EOF' | gh issue create --title Spec --label spec --body-file -\n# Spec\nRefs #7\nFull spec: sdlc-handoff/spec.md\nEOF"}
```
Must fail:
```
"name":"Bash","input":{"command":"cat > \"$TMPDIR/body.md\" <<'EOF'\n# Spec\nFull spec: /tmp/sdlc-ab/spec.md\nEOF"}
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body-file=\"$TMPDIR/body.md\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"$( { cat sdlc-handoff/spec.md; printf '\\n\\nRefs #7\\n'; } )\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"$(cat sdlc-handoff/spec.md | sed -e 's|in this run.s folder|in #7|')\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"$(tail -n +2 /tmp/sdlc-ab/spec.md && echo && echo Refs \#7)\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"$(cat sdlc-handoff/spec.md; echo; echo Full spec: /tmp/sdlc-ab/spec.md)\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"$(printf \"Full spec: %s\" /tmp/sdlc-ab/spec.md)\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title Spec --label spec --body \"$(cat sdlc-handoff/spec.md)\n\nFull spec: $(echo /tmp/sdlc-ab/spec.md)\""}
```
Must fail:
```
"name":"Bash","input":{"command":"echo \"$(cat sdlc-handoff/spec.md)\" $(printf 'see %s' /tmp/sdlc-ab/spec.md) | gh issue create --title Spec --label spec --body-file -"}
```
### docs-say/graders/shape-issue-body-is-spec.md
Must pass:
```
"name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } > \"$TMPDIR/spec-issue-body.md\" && gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file \"$TMPDIR/spec-issue-body.md\"","description":"File the approved spec as a GitHub issue linked to #7","allowed_domains":["api.github.com","github.com"]}
```
Must pass:
```
"name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } | gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file -","description":"File the approved spec as a GitHub issue linked to #7"}
```
Must pass:
```
"name":"Write","input":{"file_path":"/tmp/claude-eval-oeEYLm/tmp/claude-0/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md","content":"Refs #7\n\n# Spec — CSV export of all orders\n\n**Intent:** story #7 (S1: export the order book for accounting), one delivery.\n\n**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:\n[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.\n\n**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.\n\n## Functional spec\n\n`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.\n\n## Acceptance criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | S1 | [1][3] | unittest |\n| C2 | every order in `data/orders.json` appears exactly once, in `list` order (1001, 1002, 1003, 1004, 1005) | S1 | [1][3] | unittest |\n| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | S1 | [4] | unittest |\n| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | S1 | [4] | unittest |\n| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | S1 | [5] | unittest |\n\n## Preservation criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| P1 | `python3 -m orders list` output is byte-identical to the base | S1 | [7] | `diff <(git show <base>:… run) <(python3 -m orders list)`: the base's output captured at the test gate, compared at the head |\n| P2 | `data/orders.json` is unchanged | S1 | [7] | `git diff --exit-code <base> -- data/orders.json` |\n| P3 | the existing suite passes | S1 | [7][8] | `python3 -m unittest discover -s tests` |\n\n## Edge cases\n\n| id | case | story | branch | check |\n|---|---|---|---|---|\n| E1 | `export` without `--csv` exits non-zero with a usage message | S1 | [6] | unittest |\n| E2 | an unwritable path exits non-zero with the OS error on stderr, no traceback | S1 | [6] | unittest |\n"}
"name":"Bash","input":{"command":"gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file /tmp/claude-eval-oeEYLm/tmp/claude-0/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md 2>&1; echo \"exit=$?\"","description":"File the approved spec as a GitHub issue labelled spec","allowed_domains":["api.github.com","github.com"]}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body \"$(cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n')\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec: CSV export\" --label spec --body-file sdlc-handoff/spec.md"}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec: CSV export\" --label spec --body-file - < \"$TMPDIR/sdlc-3f2a/spec.md\""}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec: CSV export\" --label spec --body '# Spec — CSV export of all orders\n\n**Intent:** `intent.md` in this run's folder: S1 (export the order book for accounting, issue #7), one delivery.\n\n**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:\n[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.\n\n**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.\n\n## Functional spec\n\n`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.\n\n## Acceptance criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | S1 | [1][3] | unittest |\n| C2 | every order in `data/orders.json` appears exactly once, in `list` order (1001, 1002, 1003, 1004, 1005) | S1 | [1][3] | unittest |\n| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | S1 | [4] | unittest |\n| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | S1 | [4] | unittest |\n| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | S1 | [5] | unittest |\n\n## Preservation criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| P1 | `python3 -m orders list` output is byte-identical to the base | S1 | [7] | `diff <(git show <base>:… run) <(python3 -m orders list)`: the base's output captured at the test gate, compared at the head |\n| P2 | `data/orders.json` is unchanged | S1 | [7] | `git diff --exit-code <base> -- data/orders.json` |\n| P3 | the existing suite passes | S1 | [7][8] | `python3 -m unittest discover -s tests` |\n\n## Edge cases\n\n| id | case | story | branch | check |\n|---|---|---|---|---|\n| E1 | `export` without `--csv` exits non-zero with a usage message | S1 | [6] | unittest |\n| E2 | an unwritable path exits non-zero with the OS error on stderr, no traceback | S1 | [6] | unittest |\n\nRefs #7'"}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec: CSV export\" --label spec --body \"CSV export of all orders: criteria C1–C5 agreed, see the spec. Refs #7\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body \"See $TMPDIR/sdlc-3f2a/spec.md. Refs #7\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/issue.md\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --title \"Spec: CSV export\" --label spec --body '# Spec — CSV export of all orders\n\n**Intent:** `intent.md` in this run's folder: S1 (export the order book for accounting, the story issue), one delivery.\n\n**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:\n[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.\n\n**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.\n\n## Functional spec\n\n`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.\n\n## Acceptance criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | S1 | [1][3] | unittest |\n| C2 | every order in `data/orders.json` appears exactly once, in `list` order (1001, 1002, 1003, 1004, 1005) | S1 | [1][3] | unittest |\n| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | S1 | [4] | unittest |\n| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | S1 | [4] | unittest |\n| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | S1 | [5] | unittest |\n\n## Preservation criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| P1 | `python3 -m orders list` output is byte-identical to the base | S1 | [7] | `diff <(git show <base>:… run) <(python3 -m orders list)`: the base's output captured at the test gate, compared at the head |\n| P2 | `data/orders.json` is unchanged | S1 | [7] | `git diff --exit-code <base> -- data/orders.json` |\n| P3 | the existing suite passes | S1 | [7][8] | `python3 -m unittest discover -s tests` |\n\n## Edge cases\n\n| id | case | story | branch | check |\n|---|---|---|---|---|\n| E1 | `export` without `--csv` exits non-zero with a usage message | S1 | [6] | unittest |\n| E2 | an unwritable path exits non-zero with the OS error on stderr, no traceback | S1 | [6] | unittest |\n'"}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/issue.md","content":"# Spec — CSV export of all orders\n\n**Intent:** `intent.md` in this run's folder: S1 (export the order book for accounting, the story issue), one delivery.\n\n**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:\n[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.\n\n**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.\n\n## Functional spec\n\n`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.\n\n## Acceptance criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | S1 | [1][3] | unittest |\n| C2 | every order in `data/orders.json` appears exactly once, in `list` order (1001, 1002, 1003, 1004, 1005) | S1 | [1][3] | unittest |\n| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | S1 | [4] | unittest |\n| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | S1 | [4] | unittest |\n| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | S1 | [5] | unittest |\n\n## Preservation criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| P1 | `python3 -m orders list` output is byte-identical to the base | S1 | [7] | `diff <(git show <base>:… run) <(python3 -m orders list)`: the base's output captured at the test gate, compared at the head |\n| P2 | `data/orders.json` is unchanged | S1 | [7] | `git diff --exit-code <base> -- data/orders.json` |\n| P3 | the existing suite passes | S1 | [7][8] | `python3 -m unittest discover -s tests` |\n\n## Edge cases\n\n| id | case | story | branch | check |\n|---|---|---|---|---|\n| E1 | `export` without `--csv` exits non-zero with a usage message | S1 | [6] | unittest |\n| E2 | an unwritable path exits non-zero with the OS error on stderr, no traceback | S1 | [6] | unittest |\n"}
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/issue.md\""}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/issue.md","content":"# Spec — CSV export of all orders\n\n**Intent:** `intent.md` in this run's folder: S1 (export the order book for accounting, issue #7), one delivery.\n\n**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:\n[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.\n\n**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.\n\n## Functional spec\n\n`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.\n\n## Acceptance criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | S1 | [1][3] | unittest |\n| C2 | every order in `data/orders.json` appears exactly once, in `list` order (1001, 1002, 1003, 1004, 1005) | S1 | [1][3] | unittest |\n| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | S1 | [4] | unittest |\n| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | S1 | [4] | unittest |\n| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | S1 | [5] | unittest |\n\n## Preservation criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| P1 | `python3 -m orders list` output is byte-identical to the base | S1 | [7] | `diff <(git show <base>:… run) <(python3 -m orders list)`: the base's output captured at the test gate, compared at the head |\n| P2 | `data/orders.json` is unchanged | S1 | [7] | `git diff --exit-code <base> -- data/orders.json` |\n| P3 | the existing suite passes | S1 | [7][8] | `python3 -m unittest discover -s tests` |\n\n## Edge cases\n\n| id | case | story | branch | check |\n|---|---|---|---|---|\n| E1 | `export` without `--csv` exits non-zero with a usage message | S1 | [6] | unittest |\n| E2 | an unwritable path exits non-zero with the OS error on stderr, no traceback | S1 | [6] | unittest |\n\nRefs #7\n"}
"name":"Bash","input":{"command":"gh issue create --title \"Spec\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/summary.md\""}
```
Must fail:
```
"name":"Bash","input":{"command":"cat sdlc-handoff/spec.md > /dev/null && gh issue create --title \"Spec\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/summary.md\""}
```
Must fail:
```
"name":"Bash","input":{"command":"cat sdlc-handoff/spec.md; printf 'Refs #7'"}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue view 7"}
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/spec.md","content":"# Spec — CSV export of all orders\n\n**Intent:** `intent.md` in this run's folder: S1 (export the order book for accounting, issue #7), one delivery.\n\n**Design tree:** 8 branches, all decided (design interview). Branch numbers below refer to it:\n[1] scope and non-goals · [2] consumer · [3] columns and order · [4] quoting and encoding · [5] money and dates · [6] errors · [7] preservation · [8] testing.\n\n**Assumptions:** A1 — accounting's importer accepts RFC 4180 quoting. Stops holding when an import rejects a quoted field.\n\n## Functional spec\n\n`python3 -m orders export --csv <path>` writes every order in `data/orders.json` to `<path>` as UTF-8 CSV without a byte-order mark, comma-separated, RFC 4180 quoting, with the header `id,customer,total,placed_on` and rows in `list` order. Out of scope: filtering, other formats, stdout.\n\n## Acceptance criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| C1 | `python3 -m orders export --csv <path>` exits 0 and the file's first line is `id,customer,total,placed_on` | S1 | [1][3] | unittest |\n| C2 | every order in `data/orders.json` appears exactly once, in `list` order (1001, 1002, 1003, 1004, 1005) | S1 | [1][3] | unittest |\n| C3 | `Berg, Hanna` is written quoted and reads back through `csv.reader` as one field | S1 | [4] | unittest |\n| C4 | the file is UTF-8 without a BOM; `Åkesson & Dotter` reads back unchanged | S1 | [4] | unittest |\n| C5 | totals keep two decimals (`89.50`, `15.00`); dates are ISO (`2026-09-03`) | S1 | [5] | unittest |\n\n## Preservation criteria\n\n| id | criterion | story | branch | check |\n|---|---|---|---|---|\n| P1 | `python3 -m orders list` output is byte-identical to the base | S1 | [7] | `diff <(git show <base>:… run) <(python3 -m orders list)`: the base's output captured at the test gate, compared at the head |\n| P2 | `data/orders.json` is unchanged | S1 | [7] | `git diff --exit-code <base> -- data/orders.json` |\n| P3 | the existing suite passes | S1 | [7][8] | `python3 -m unittest discover -s tests` |\n\n## Edge cases\n\n| id | case | story | branch | check |\n|---|---|---|---|---|\n| E1 | `export` without `--csv` exits non-zero with a usage message | S1 | [6] | unittest |\n| E2 | an unwritable path exits non-zero with the OS error on stderr, no traceback | S1 | [6] | unittest |\n"}
```

### docs-say/graders/shape-one-gh-issue-create.md
Must pass:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01PyTrPcSYgqfznqi1KhqC4T","name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } > \"$TMPDIR/spec-issue-body.md\" && gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file \"$TMPDIR/spec-issue-body.md\"","description":"File the approved spec as a GitHub issue linked to #7","allowed_domains":["api.github.com","github.com"]},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"<tool_use_error>allowed_domains cannot widen network access in this session: the configured sandbox allowlist is the whole allowlist here (a managed-domains-only or strictAllowlist policy, or a confined evaluation run). Remove allowed_domains and use a host the configured allowlist already covers.</tool_use_error>","is_error":true,"tool_use_id":"toolu_01PyTrPcSYgqfznqi1KhqC4T"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_013Ej5JvHdMDWYz5XM1VSmX6","name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } > \"$TMPDIR/spec-issue-body.md\" && gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file \"$TMPDIR/spec-issue-body.md\"","description":"File the approved spec as a GitHub issue linked to #7"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\n/bin/bash: line 1: /tmp/claude-eval-YPFmx5/tmp/claude-0/spec-issue-body.md: Read-only file system","is_error":true,"tool_use_id":"toolu_013Ej5JvHdMDWYz5XM1VSmX6"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01QVPa7L5BSx5SJfjGwYp9RB","name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } | gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file -","description":"File the approved spec as a GitHub issue linked to #7"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01QVPa7L5BSx5SJfjGwYp9RB"}]}}
```
Must pass:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01ALyDu9he61NjVZKrEKNLia","name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } > \"$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md\" && gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec — CSV export of all orders\" --label spec --body-file \"$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md\"","description":"File the approved spec as a GitHub issue linked to #7","allowed_domains":["api.github.com","github.com"]},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"<tool_use_error>allowed_domains cannot widen network access in this session: the configured sandbox allowlist is the whole allowlist here (a managed-domains-only or strictAllowlist policy, or a confined evaluation run). Remove allowed_domains and use a host the configured allowlist already covers.</tool_use_error>","is_error":true,"tool_use_id":"toolu_01ALyDu9he61NjVZKrEKNLia"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01L4Q2AqeBSUaufFLHhT371E","name":"Bash","input":{"command":"gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec — CSV export of all orders\" --label spec --body-file \"$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md\"","description":"File the approved spec as a GitHub issue labelled spec"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01L4Q2AqeBSUaufFLHhT371E"}]}}
```
Must pass:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01SWiR68J5KfBnM8emkATVFw","name":"Bash","input":{"command":"gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file /tmp/claude-eval-oeEYLm/tmp/claude-0/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md 2>&1; echo \"exit=$?\"","description":"File the approved spec as a GitHub issue labelled spec","allowed_domains":["api.github.com","github.com"]},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"<tool_use_error>allowed_domains cannot widen network access in this session: the configured sandbox allowlist is the whole allowlist here (a managed-domains-only or strictAllowlist policy, or a confined evaluation run). Remove allowed_domains and use a host the configured allowlist already covers.</tool_use_error>","is_error":true,"tool_use_id":"toolu_01SWiR68J5KfBnM8emkATVFw"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01W4oJJzVTGBotKqDQBaoStc","name":"Bash","input":{"command":"gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file /tmp/claude-eval-oeEYLm/tmp/claude-0/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md 2>&1; echo \"exit=$?\"","description":"File the approved spec as a GitHub issue labelled spec"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\nexit=1\n/bin/bash: line 1: /tmp/claude-eval-oeEYLm/tmp/claude-0/cwd-7977: Read-only file system\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01W4oJJzVTGBotKqDQBaoStc"}]}}
```
Must fail:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01PyTrPcSYgqfznqi1KhqC4T","name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } > \"$TMPDIR/spec-issue-body.md\" && gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file \"$TMPDIR/spec-issue-body.md\"","description":"File the approved spec as a GitHub issue linked to #7","allowed_domains":["api.github.com","github.com"]},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"<tool_use_error>allowed_domains cannot widen network access in this session: the configured sandbox allowlist is the whole allowlist here (a managed-domains-only or strictAllowlist policy, or a confined evaluation run). Remove allowed_domains and use a host the configured allowlist already covers.</tool_use_error>","is_error":true,"tool_use_id":"toolu_01PyTrPcSYgqfznqi1KhqC4T"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_013Ej5JvHdMDWYz5XM1VSmX6","name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } > \"$TMPDIR/spec-issue-body.md\" && gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file \"$TMPDIR/spec-issue-body.md\"","description":"File the approved spec as a GitHub issue linked to #7"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\n/bin/bash: line 1: /tmp/claude-eval-YPFmx5/tmp/claude-0/spec-issue-body.md: Read-only file system","is_error":true,"tool_use_id":"toolu_013Ej5JvHdMDWYz5XM1VSmX6"}]}}
```
Must fail:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01W4oJJzVTGBotKqDQBaoStc","name":"Bash","input":{"command":"gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file /tmp/claude-eval-oeEYLm/tmp/claude-0/sdlc-00000000-0000-4000-8000-0000000000aa/spec-issue-body.md 2>&1; echo \"exit=$?\"","description":"File the approved spec as a GitHub issue labelled spec"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\nexit=1\n/bin/bash: line 1: /tmp/claude-eval-oeEYLm/tmp/claude-0/cwd-7977: Read-only file system\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01W4oJJzVTGBotKqDQBaoStc"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01QVPa7L5BSx5SJfjGwYp9RB","name":"Bash","input":{"command":"{ cat sdlc-handoff/spec.md; printf '\\nRefs #7\\n'; } | gh issue create --repo example/ordersdesk-gh-tracker --title \"Spec: CSV export of all orders\" --label spec --body-file -","description":"File the approved spec as a GitHub issue linked to #7"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nGraphQL: Could not resolve to a Repository with the name 'example/ordersdesk-gh-tracker'. (repository)","is_error":true,"tool_use_id":"toolu_01QVPa7L5BSx5SJfjGwYp9RB"}]}}
```

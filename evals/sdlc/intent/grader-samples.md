# Grader samples — Intent

Offline samples for every regex shape grader in this scenario; `python3 evals/sdlc/tools/test_shape_graders.py` checks them. The `tool_used` graders' `input_match` patterns are not checked by it; their samples are kept here as documentation:

- `shape-no-write-outside-docs` / `shape-no-edit-outside-docs` `"file_path":\s*"(?![^"]*/sdlc(?:/|-(?!handoff/)))` matches (a violation) `"file_path": "/work/ordersdesk/orders/__main__.py"` and `"file_path": "/work/ordersdesk/sdlc-handoff/intent.md"`; it does not match `"file_path": "/var/folders/xy/T/sdlc-3f2a/intent.md"`.
- `shape-one-gh-issue-create` / `shape-no-gh-issue-create` `\bgh\s+issue\s+create\b` matches `{"command": "gh issue create --title \"Find a customer's orders\" --label story --body-file \"$TMPDIR/sdlc-3f2a/s2.md\""}`; it does not match `{"command": "gh auth status"}` or `{"command": "gh issue list --label story"}`.
- `shape-no-gh-issue` `\bgh\s+(?:issue\b|api\b[^\n]*\bissues\b)` matches `{"command": "gh issue view 42"}`, `{"command": "gh issue edit 42 --body-file x.md"}` and `{"command": "gh api repos/example/ordersdesk/issues -f title=x"}`; it does not match `{"command": "gh auth status"}` or `{"command": "git log --oneline"}`.
- `shape-interview-once` / `shape-interview-invoked` match a Skill call whose input holds `design-interview`, such as `{"skill": "design:design-interview"}`.

`shape-filed-body-is-s2` is a regex grader over the whole trace, not a judged one: a judge of a long resumed run sees only the trace's head and tail (about 23 KB), and the filing call sits in between. It matches the compact tool call as `trace.jsonl` writes it (`"name":"Bash","input":{"command":"…"}`), its body inline in that command, or in a file a Write or Bash call wrote earlier and the `gh issue create` reads by `--body-file`/`-F` under the same file name. The body must hold S2 (`back-office clerk` or its story line, and `--customer`) and nothing of S1 or S3 (`accountant`, `export --csv`, `shop manager`, `orders daily`, `takings`).

### idea/graders/shape-phase-intent.md
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "intent\n"}
```
Must pass:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/phase\",\"content\":\"intent\"}
```
Must pass:
```
mkdir -p "$TMPDIR/sdlc-3f2a" && echo intent > "$TMPDIR/sdlc-3f2a/phase"
```
Must pass:
```
D="$TMPDIR/sdlc-3f2a"; mkdir -p "$D" && printf 'intent\n' > "$D/phase"
```
Must pass:
```
{"file_path": "/private/tmp/claude-501/x/scratchpad/sdlc/phase", "content": "intent\n"}
```
Must fail:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "spec\n"}
```
Must fail:
```
echo intent > "/work/ordersdesk/sdlc-handoff/phase"
```
Must fail:
```
echo intent > "$TMPDIR/sdlc-3f2a/intent.md"
```
Must fail:
```
The phase file `$TMPDIR/sdlc-…/phase` will say intent.
```

### idea/graders/shape-intent-written.md
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e-0b7d-4e8a-9c1f-2d4e6a8b0c12/intent.md", "content": "# Intent"}
```
Must pass:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/intent.md\",\"content\":\"# Intent\"}
```
Must pass:
```
cat > "$TMPDIR/sdlc-3f2a9c1e/intent.md" <<'EOF'
```
Must pass:
```
{"file_path": "/private/tmp/claude-501/x/scratchpad/sdlc/intent.md", "content": "# Intent"}
```
Must fail:
```
{"file_path": "/work/ordersdesk/sdlc-handoff/intent.md", "content": "# Intent"}
```
Must fail:
```
{"file_path": "/work/ordersdesk/docs/intent.md", "content": "# Intent"}
```
Must fail:
```
The stories will live at `$TMPDIR/sdlc-…/intent.md`.
```
Must fail:
```
cat "$TMPDIR/sdlc-3f2a/intent.md"
```
Must fail:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a/spec.md", "content": "# Spec"}
```

### just-go/graders/shape-intent-written.md
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/intent.md", "content": "# Intent"}
```
Must pass:
```
cat > "$TMPDIR/sdlc-3f2a9c1e/intent.md" <<'EOF'
```
Must fail:
```
{"file_path": "/work/ordersdesk/sdlc-handoff/intent.md", "content": "# Intent"}
```
Must fail:
```
cat "$TMPDIR/sdlc-3f2a/intent.md"
```

### story-ticket/graders/shape-intent-written.md
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/intent.md", "content": "# Intent"}
```
Must pass:
```
cat > "$TMPDIR/sdlc-3f2a9c1e/intent.md" <<'EOF'
```
Must fail:
```
{"file_path": "/work/ordersdesk/sdlc-handoff/intent.md", "content": "# Intent"}
```
Must fail:
```
cat "$TMPDIR/sdlc-3f2a/intent.md"
```

### all-dropped/graders/shape-phase-done.md
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "done\n"}
```
Must pass:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/phase\",\"content\":\"done\"}
```
Must pass:
```
printf done > "$TMPDIR/sdlc-3f2a/phase"
```
Must pass:
```
D="$TMPDIR/sdlc-3f2a"; mkdir -p "$D" && echo done > "$D/phase"
```
Must fail:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "intent\n"}
```
Must fail:
```
echo done > "/work/ordersdesk/sdlc-handoff/phase"
```
Must fail:
```
cat "$TMPDIR/sdlc-3f2a/phase"
```
Must fail:
```
Every story is dropped, so the run is done.
```

### dispositions/graders/shape-filed-body-is-s2.md
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body 'As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\n- `python3 -m orders list` without `--customer` prints what it prints today.\n\nNotes: partial names are enough (\"berg\" finds \"Berg, Hanna\").' 2>&1","description":"File story S2 as a GitHub issue"}
```
Must pass:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/s2-issue.md","content":"## S2 — Find a customer's orders\n\nAs a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\n"}
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body-file \"$TMPDIR/sdlc-3f2a/s2-issue.md\""}
```
Must pass:
```
"name":"Bash","input":{"command":"cat > \"$TMPDIR/sdlc-3f2a/s2.md\" <<'EOF'\nAs a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\nEOF"}
"name":"Bash","input":{"command":"gh issue create --label story --title \"Find a customer's orders\" -F \"$TMPDIR/sdlc-3f2a/s2.md\" 2>&1"}
```
Must pass:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2\" --body-file - <<'EOF'\nAs a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\nEOF"}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"S1 — Export the order book\" --body 'As an accountant, I want every order exported as a CSV file I can feed to our importer, so that I stop retyping orders at month end.\n\nAcceptance criteria:\n- `python3 -m orders export --csv <path>` writes every order in the book to `<path>` with a header row.'"}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body 'As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\n\nAs the shop manager, I want the total of each day's orders, so that I can compare days without a spreadsheet.\n\nAcceptance criteria:\n- `python3 -m orders daily` prints one line per day that has orders.'"}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"Back-office stories\" --body 'As an accountant, I want every order exported as a CSV file I can feed to our importer, so that I stop retyping orders at month end.\n\nAcceptance criteria:\n- `python3 -m orders export --csv <path>` writes every order in the book to `<path>` with a header row.\n\nAs a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.'"}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body-file \"$TMPDIR/sdlc-3f2a/s2.md\""}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"See sdlc-handoff/intent.md, S2 (back-office clerk).\""}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/s2.md","content":"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\n"}
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2\" --body-file \"$TMPDIR/sdlc-3f2a/s3.md\""}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/s2.md","content":"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\n"}
```
Must fail:
```
"name":"Bash","input":{"command":"gh issue create --label story --title \"S2\" --body-file \"$TMPDIR/sdlc-3f2a/s2.md\""}
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/s2.md","content":"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- `python3 -m orders list --customer <text>` prints only orders whose customer contains `<text>`, ignoring case.\n- No match prints nothing and exits 0.\n"}
```
Must fail:
```
{"type":"text","text":"Filing S2: As a back-office clerk, I want to list only the orders of the customer I name. `python3 -m orders list --customer <text>`. Next: gh issue create."}
```


# Grader samples — Intent

Offline samples for every regex shape grader in this scenario; `python3 evals/sdlc/tools/test_shape_graders.py` checks them. The `tool_used` graders' `input_match` patterns are not checked by it; their samples are kept here as documentation:

- `shape-no-write-outside-docs` / `shape-no-edit-outside-docs` `"file_path":\s*"(?![^"]*/sdlc(?:/|-(?!handoff/)))` matches (a violation) `"file_path": "/work/ordersdesk/orders/__main__.py"` and `"file_path": "/work/ordersdesk/sdlc-handoff/intent.md"`; it does not match `"file_path": "/var/folders/xy/T/sdlc-3f2a/intent.md"`.
- `shape-no-gh-issue-create` `\bgh\s+(?:issue\s+create\b|api\b[^\n]*\bissues\b)` matches `{"command": "gh issue create --title \"Find a customer's orders\" --label story --body-file \"$TMPDIR/sdlc-3f2a/s2.md\""}` and `{"command": "gh api repos/example/ordersdesk/issues -f title=\"Find a customer's orders\" -f body=x"}`; it does not match `{"command": "gh auth status"}` or `{"command": "gh issue list --label story"}`.
- `shape-no-gh-issue-write` (`ticket-says-file`) `\bgh\s+(?:issue\s+(?:create|edit|comment|close|reopen|delete|transfer)\b|api\b(?=[^\n]*\bissues\b)(?=[^\n]*\s(?:-X\s*(?!GET\b)[A-Za-z]|--method[\s=]+(?!GET\b)[A-Za-z]|-[fF]\s|--(?:field|raw-field|input)\b)))` matches a write to the tracker: `{"command": "gh issue edit 42 --body-file x.md"}`, `{"command": "gh issue comment 42 --body \"Filed in OPS\""}`, `{"command": "gh api repos/example/ordersdesk/issues -f title=x"}` and `{"command": "gh api -X PATCH repos/example/ordersdesk/issues/42 -F body=@x.md"}`; it does not match reading the ticket, `{"command": "gh issue view 42 --json title,body"}` or `{"command": "gh api repos/example/ordersdesk/issues/42"}`, nor `{"command": "gh auth status"}`. Reading ticket #42 is how a run gets its text, so only writes count.
- `shape-gh-issue-create-attempted` (`all-filed`, `min: 1`) `\bgh\s+(?:issue\s+create\b|api\b[^\n]*\bissues\b)` matches `{"command": "gh issue create --label story --title \"S1 — Export the order book\" --body-file \"$TMPDIR/sdlc-3f2a/s1.md\""}` and `{"command": "gh api repos/example/ordersdesk/issues -f title=\"S1 — Export the order book\" -F body=@s1.md"}`, the scenario's other tracker call; it does not match `{"command": "gh issue list --label story"}`. A count, not `shape-one-gh-issue-create`'s paired regex: it asks only that filing was tried, and a refused call is still a try.
- `shape-no-top-level-spec-write` (`next-delivery`) `"file_path":\s*"[^"]*/sdlc(?:-(?!handoff/)[^"/]*)?/spec\.md"` matches `"file_path": "/var/folders/xy/T/sdlc-3f2a/spec.md"` and `"file_path": "/private/tmp/claude-501/x/scratchpad/sdlc/spec.md"`; it does not match `"file_path": "/var/folders/xy/T/sdlc-3f2a/d2/spec.md"`. `shape-no-top-level-spec-bash` is the same for a Bash redirect, `tee`, `cp` or `mv`.
- `shape-no-jira-call` (`ticket-says-file`) `\b(?:curl|wget|http)\b[^\n]*(?:atlassian|jira)|\b(?:jira|acli)\s+(?:issue|workitem|create)\b` matches `{"command": "curl -X POST https://example.atlassian.net/rest/api/3/issue -d @s2.json"}` and `{"command": "jira issue create -p OPS -t Story"}`; it does not match `{"command": "grep -ri jira CLAUDE.md README.md"}`.
- `shape-interview-once` / `shape-interview-invoked` match a Skill call whose input holds `design-interview`, such as `{"skill": "design:design-interview"}`; `shape-no-interview` is the same pattern at `max: 0` (`next-delivery`'s prompt says the change is small, which skips the interview).

`shape-filed-body-is-s2` is a regex grader over the whole trace, not a judged one: a judge of a long resumed run sees only the trace's head and tail (about 23 KB), and the filing call sits in between. It matches the compact tool call as `trace.jsonl` writes it (`"name":"Bash","input":{"command":"…"}`), its body inline in that command, or in a file a Write or Bash call wrote earlier and the `gh issue create` reads by `--body-file`/`-F` under the same file name. The body must hold S2 (`back-office clerk` or its story line, and `--customer`) and nothing of S1 or S3 (`accountant`, `export --csv`, `shop manager`, `orders daily`, `takings`).

`shape-one-gh-issue-create` is a regex grader over the whole trace, not a `tool_used` count: a count also took Bash calls the harness refused before running them (a `<tool_use_error>`, such as `allowed_domains cannot widen network access`) and calls where `gh` never ran (a `> "$TMPDIR/…" && gh issue create …` whose redirect failed with `Read-only file system`), so a run that filed once was failed for its retries. It pairs each `gh issue create` Bash call (`"id":"toolu_…","name":"Bash","input":{"command":"…"`) with its `tool_result` by `tool_use_id`, in either key order, and counts the call as a filing attempt when the result is not a `<tool_use_error>` or a `Permission to use` refusal, and either shows `gh` ran (`api.github.com`, an issue URL, `gh auth login`, `GH_TOKEN`, `GraphQL:`, `HTTP 4xx/5xx`, `could not add label`) or carries no shell error (`bash: line N: `, `zsh:N: `, `sh: `) other than the harness's own `…/cwd-…: ` file. Anchored at the trace's start, it passes when such an attempt exists and no second one with another id does. `shape-no-gh-issue-create` and `shape-no-gh-issue-write` stay `tool_used` counts: there a refused call is still an attempt to file.

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

### ticket-says-file/graders/shape-intent-written.md
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

### all-filed/graders/shape-phase-done.md
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

### next-delivery/graders/shape-phase-not-done.md
Must fail:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "done\n"}
```
Must fail:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/phase\",\"content\":\"done\"}
```
Must fail:
```
printf done > "$TMPDIR/sdlc-3f2a/phase"
```
Must fail:
```
D="$TMPDIR/sdlc-3f2a"; mkdir -p "$D" && echo done > "$D/phase"
```
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "intent\n"}
```
Must pass:
```
echo done > "/work/ordersdesk/sdlc-handoff/phase"
```
Must pass:
```
cat "$TMPDIR/sdlc-3f2a/phase"
```
Must pass:
```
Every story is dropped, so the run is done.
```

### next-delivery/graders/shape-d2-folder.md
Must pass:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a9c1e/d2/spec.md","content":"# Spec — find a customer's orders"}
```
Must pass:
```
"name":"Write","input":{"file_path":"/private/tmp/claude-501/x/scratchpad/sdlc/d2/phase","content":"spec"}
```
Must pass:
```
"name":"Edit","input":{"replace_all":false,"file_path":"/var/folders/xy/T/sdlc-3f2a/d2/notes.md","old_string":"a","new_string":"b"}
```
Must pass:
```
"name":"Bash","input":{"command":"mkdir -p \"$TMPDIR/sdlc-3f2a/d2\"","description":"Make delivery d2's folder"}
```
Must pass:
```
"name":"Bash","input":{"command":"cat > \"$TMPDIR/sdlc-3f2a/d2/spec.md\" <<'EOF'\n# Spec\nEOF"}
```
Must pass:
```
"name":"Bash","input":{"command":"mkdir -p /tmp/claude-0/x/scratchpad/sdlc/d2 && cp sdlc-handoff/intent.md /tmp/claude-0/x/scratchpad/sdlc/intent.md"}
```
Must fail:
```
"name":"Bash","input":{"command":"mkdir -p sdlc-handoff/d2"}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a9c1e/intent.md","content":"| d2 | S2 | in progress |"}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a9c1e/spec.md","content":"# Spec — find a customer's orders"}
```
Must fail:
```
"name":"Write","input":{"file_path":"/work/ordersdesk-csv-export-branch/sdlc-handoff/d2/spec.md","content":"# Spec"}
```
Must fail:
```
"name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a9c1e/d1/spec.md","content":"# Spec"}
```
Must fail:
```
"name":"Bash","input":{"command":"ls \"$TMPDIR/sdlc-3f2a/d2\""}
```
Must fail:
```
d2's documents will go in `$TMPDIR/sdlc-3f2a/d2/`.
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

### dispositions/graders/shape-one-gh-issue-create.md
Must pass:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01M37fYZUNrDBmntE7gEgjgb","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story","allowed_domains":["api.github.com"]},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"<tool_use_error>allowed_domains cannot widen network access in this session: the configured sandbox allowlist is the whole allowlist here (a managed-domains-only or strictAllowlist policy, or a confined evaluation run). Remove allowed_domains and use a host the configured allowlist already covers.</tool_use_error>","is_error":true,"tool_use_id":"toolu_01M37fYZUNrDBmntE7gEgjgb"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01Q19GBUGs65FCG1U3H45f3q","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01Q19GBUGs65FCG1U3H45f3q"}]}}
```
Must pass:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01BMWP3KM1C6tGzxaL12FXsH","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01BMWP3KM1C6tGzxaL12FXsH"}]}}
```
Must pass:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01A","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","tool_use_id":"toolu_01A","content":"Exit code 4\nTo get started with GitHub CLI, please run:  gh auth login\nAlternatively, populate the GH_TOKEN environment variable with a GitHub API authentication token.","is_error":true}]}}
```
Must pass:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01A","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"https://github.com/example/ordersdesk/issues/12","is_error":false,"tool_use_id":"toolu_01A"}]}}
```
Must fail:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01M37fYZUNrDBmntE7gEgjgb","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story","allowed_domains":["api.github.com"]},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"<tool_use_error>allowed_domains cannot widen network access in this session: the configured sandbox allowlist is the whole allowlist here (a managed-domains-only or strictAllowlist policy, or a confined evaluation run). Remove allowed_domains and use a host the configured allowlist already covers.</tool_use_error>","is_error":true,"tool_use_id":"toolu_01M37fYZUNrDBmntE7gEgjgb"}]}}
```
Must fail:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01BMWP3KM1C6tGzxaL12FXsH","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01BMWP3KM1C6tGzxaL12FXsH"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01Q19GBUGs65FCG1U3H45f3q","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\"","description":"File story S2 as a GitHub issue labelled story"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nPost \"https://api.github.com/graphql\": user denied\n\n<sandbox_violations>\ndeny network-outbound api.github.com:443 (user denied)\n</sandbox_violations>","is_error":true,"tool_use_id":"toolu_01Q19GBUGs65FCG1U3H45f3q"}]}}
```
Must fail:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01A","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\""}},{"type":"tool_use","id":"toolu_01B","name":"Bash","input":{"command":"gh issue create --label story --title \"S2 — Find a customer's orders\" --body \"As a back-office clerk, I want to list only the orders of the customer I name, so that I can answer a customer on the phone without scrolling the whole book.\n\nAcceptance criteria:\n- \\`python3 -m orders list --customer <text>\\` prints only orders whose customer contains \\`<text>\\`, ignoring case.\""}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"https://github.com/example/ordersdesk/issues/12","is_error":false,"tool_use_id":"toolu_01A"},{"type":"tool_result","content":"https://github.com/example/ordersdesk/issues/13","is_error":false,"tool_use_id":"toolu_01B"}]}}
```
Must fail:
```
{"type":"assistant","message":{"role":"assistant","content":[{"type":"tool_use","id":"toolu_01A","name":"Bash","input":{"command":"gh auth status","description":"Check gh auth"},"caller":{"type":"direct"}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"Exit code 1\nYou are not logged into any GitHub hosts. To log in, run: gh auth login","is_error":true,"tool_use_id":"toolu_01A"}]}}
```

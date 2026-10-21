# Grader samples — S1 CSV

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them. Each stage's author keeps the section under its own heading.

## spec

### spec/graders/shape-phase-written.md
Must pass:
```
D="$TMPDIR/sdlc-3f2a"; mkdir -p "$D" && printf spec > "$D/phase"
```
Must pass:
```
D=\"$TMPDIR/sdlc-93b6\"; mkdir -p \"$D\" && printf spec > \"$D/phase\"
```
Must fail:
```
D="/work/ordersdesk/sdlc-handoff"; echo spec > "$D/phase"
```
Must fail:
```
D="$TMPDIR/sdlc-3f2a"; cat "$D/phase"
```
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "spec\n"}
```
Must pass:
```
mkdir -p "$TMPDIR/sdlc-3f2a9c1e" && echo spec > "$TMPDIR/sdlc-3f2a9c1e/phase"
```
Must pass:
```
printf spec > \"$TMPDIR/sdlc-3f2a/phase\"
```
Must fail:
```
cat "$TMPDIR/sdlc-3f2a/phase"
```
Must fail:
```
{"file_path": "/work/ordersdesk/phase", "content": "spec"}
```
Must fail:
```
The phase file is `$TMPDIR/sdlc-…/phase`.
```

## spec-gate

### spec-gate/graders/shape-spec-written.md
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e-0b7d-4e8a-9c1f-2d4e6a8b0c12/spec.md", "content": "# Spec"}
```
Must pass:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/spec.md\",\"content\":\"# Spec\"}
```
Must pass:
```
cat > "$TMPDIR/sdlc-3f2a9c1e/spec.md" <<'EOF'
```
Must pass:
```
/private/tmp/claude-501/x/scratchpad/sdlc/spec.md written | tee /private/tmp/claude-501/x/scratchpad/sdlc/spec.md
```
Must fail:
```
{"file_path": "/work/ordersdesk/sdlc-handoff/spec.md", "content": "# Spec"}
```
Must fail:
```
{"file_path": "/work/ordersdesk/docs/spec.md", "content": "# Spec"}
```
Must fail:
```
The spec will live at `$TMPDIR/sdlc-…/spec.md` once the interview is done.
```
Must fail:
```
cat "$TMPDIR/sdlc-3f2a/spec.md"
```

## plan

### plan/graders/shape-plan-written.md
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e-0b7d-4e8a-9c1f-2d4e6a8b0c12/plan.md", "content": "# Spec"}
```
Must pass:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/plan.md\",\"content\":\"# Spec\"}
```
Must pass:
```
cat > "$TMPDIR/sdlc-3f2a9c1e/plan.md" <<'EOF'
```
Must pass:
```
/private/tmp/claude-501/x/scratchpad/sdlc/plan.md written | tee /private/tmp/claude-501/x/scratchpad/sdlc/plan.md
```
Must fail:
```
{"file_path": "/work/ordersdesk/sdlc-handoff/plan.md", "content": "# Spec"}
```
Must fail:
```
{"file_path": "/work/ordersdesk/docs/plan.md", "content": "# Spec"}
```
Must fail:
```
The spec will live at `$TMPDIR/sdlc-…/plan.md` once the interview is done.
```
Must fail:
```
cat "$TMPDIR/sdlc-3f2a/plan.md"
```
Must fail:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a/spec.md", "content": "# Spec"}
```

### plan/graders/shape-phase-plan.md
Must pass:
```
R="$TMPDIR/sdlc-3f2a"; mkdir -p "$R" && printf 'plan\n' > "$R/phase"
```
Must fail:
```
R="/work/ordersdesk/sdlc-handoff"; printf plan > "$R/phase"
```
Must fail:
```
R="$TMPDIR/sdlc-3f2a"; printf spec > "$R/phase"
```
Must pass:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "plan\n"}
```
Must pass:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/phase\",\"content\":\"plan\"}
```
Must pass:
```
mkdir -p "$TMPDIR/sdlc-3f2a" && echo plan > "$TMPDIR/sdlc-3f2a/phase"
```
Must pass:
```
printf 'plan' > $TMPDIR/sdlc-3f2a/phase
```
Must fail:
```
{"file_path": "/var/folders/xy/T/sdlc-3f2a9c1e/phase", "content": "spec\n"}
```
Must fail:
```
echo test > "$TMPDIR/sdlc-3f2a/phase" && cat "$TMPDIR/sdlc-3f2a/plan.md"
```
Must fail:
```
echo plan > "$TMPDIR/sdlc-3f2a/plan.md"
```
Must fail:
```
echo plan > phase
```


## ship

### ship/graders/shape-pr-body-file.md
Must pass:
```
{"file_path": "/T/sdlc-3f2a/pr-csv-export.md", "content": "## Summary"}
```
Must pass:
```
gh pr create --title "Export every order as CSV" --body-file "$D/pr-csv-export.md"
```
Must fail:
```
{"file_path": "/w/sdlc-handoff/pr-csv-export.md", "content": "## Summary"}
```
Must fail:
```
Write the body into the run's folder as `pr-<branch>.md`.
```
Must fail:
```
gh pr create --title "Export every order as CSV" --body "## Summary"
```

### ship/graders/shape-reply-names-fix.md
Must pass:
```
The PR was not opened: `gh` is not authenticated. Run `gh auth login`, then `gh pr create --title "Export every order as CSV" --body-file sdlc-handoff/pr-body.md`.
```
Must fail:
```
The PR was not opened: gh is not authenticated. Log in to GitHub and try again.
```

### ship/graders/shape-reply-names-body.md
Must pass:
```
The body is kept at `/var/folders/xy/T/sdlc-4f2a/pr-body.md`.
```
Must pass:
```
Body: sdlc-handoff/pr-csv-export.md
```
Must fail:
```
The spec is at sdlc-handoff/spec.md and the evidence at sdlc-handoff/evidence.md.
```
Must fail:
```
The body is kept in the docs folder.
```

## test

### test/graders/shape-phase-test.md
Must pass:
```
{"type":"tool_use","name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a9c1e/phase","content":"test\n"}}
```
Must pass:
```
{\"file_path\":\"/var/folders/xy/T/sdlc-3f2a/phase\",\"content\":\"test\"}
```
Must pass:
```
{"type":"tool_use","name":"Bash","input":{"command":"printf 'test\\n' > \"$TMPDIR/sdlc-$SID/phase\"","description":"Set the phase"}}
```
Must pass:
```
{"command":"echo test > /private/tmp/claude-501/x/scratchpad/sdlc/phase"}
```
Must fail:
```
{"file_path":"/var/folders/xy/T/sdlc-3f2a/phase","content":"plan\n"}
```
Must fail:
```
{"command":"python3 -m unittest tests.test_export > /dev/null"}
```
Must fail:
```
{"command":"echo test > out.txt"}
```

## build

### build/graders/shape-export-wired.md
Must pass:
```
    export = commands.add_parser("export", help="write every order to a file")
```
Must pass:
```
    commands.add_parser('export')
```
Must fail:
```
    commands.add_parser("list", help="print every order")
```

### build/graders/shape-security-pass.md
Must pass:
```
{"type":"tool_use","id":"toolu_1","name":"Skill","input":{"skill":"security-review"}}
```
Must pass:
```
{"type":"tool_use","id":"toolu_2","name":"Agent","input":{"description":"Security lens","prompt":"Review the diff main..HEAD for security issues","subagent_type":"general-purpose"}}
```
Must pass:
```
{\"name\":\"Skill\",\"input\":{\"skill\":\"security-review\"}}
```
Must fail:
```
{"type":"tool_use","id":"toolu_3","name":"Agent","input":{"description":"Adversarial lens","prompt":"Find bugs in the diff"}}
```
Must fail:
```
{"type":"text","text":"Next: the security pass."}
```

### build/graders/shape-test-paths-diffed.md
Must pass:
```
{"name":"Bash","input":{"command":"git diff --name-only 15418d3..HEAD -- tests/ 'test_*'","description":"x"}}
```
Must pass:
```
{"command":"/opt/homebrew/bin/git diff --stat \"$GATE\"..HEAD -- tests","description":"x"}
```
Must pass:
```
{"command":"git diff --exit-code 15418d3 HEAD -- tests/test_export.py"}
```
Must fail:
```
{"command":"git diff main"}
```
Must fail:
```
{"command":"python3 -m unittest discover -s tests"}
```
Must fail:
```
{"command":"git diff 15418d3..HEAD -- orders/"}
```

### plan/graders/shape-no-commit.md
Must pass:
```
{"command": "git commit -m x"}
```
Must pass:
```
{"command": "/opt/homebrew/bin/git -C \"$R\" commit -qm x"}
```
Must pass:
```
{"command": "G=/opt/homebrew/bin/git; $G add README.md && $G commit -q"}
```
Must fail:
```
{"command": "cat .git/refs/heads/main", "description": "Check the base commit"}
```
Must fail:
```
{"command": "git diff --quiet ea4086f -- data/orders.json", "description": "Check against the base commit"}
```
Must fail:
```
{"command": "git log --oneline"}
```

### spec-gate/graders/shape-no-commit.md
Must pass:
```
{"command": "git commit -m x"}
```
Must pass:
```
{"command": "/opt/homebrew/bin/git -C \"$R\" commit -qm x"}
```
Must pass:
```
{"command": "G=/opt/homebrew/bin/git; $G add README.md && $G commit -q"}
```
Must fail:
```
{"command": "cat .git/refs/heads/main", "description": "Check the base commit"}
```
Must fail:
```
{"command": "git diff --quiet ea4086f -- data/orders.json", "description": "Check against the base commit"}
```
Must fail:
```
{"command": "git log --oneline"}
```

### spec/graders/shape-no-commit.md
Must pass:
```
{"command": "git commit -m x"}
```
Must pass:
```
{"command": "/opt/homebrew/bin/git -C \"$R\" commit -qm x"}
```
Must pass:
```
{"command": "G=/opt/homebrew/bin/git; $G add README.md && $G commit -q"}
```
Must fail:
```
{"command": "cat .git/refs/heads/main", "description": "Check the base commit"}
```
Must fail:
```
{"command": "git diff --quiet ea4086f -- data/orders.json", "description": "Check against the base commit"}
```
Must fail:
```
{"command": "git log --oneline"}
```

### ship/graders/shape-auth-before-push.md
Must pass:
```
{"name":"Bash","input":{"command":"gh auth status 2>&1"}}
{"name":"Bash","input":{"command":"/opt/homebrew/bin/git push -u origin csv-export"}}
```
Must pass:
```
{"name":"Bash","input":{"command":"gh auth status 2>&1"}}
```
Must fail:
```
{"name":"Bash","input":{"command":"/opt/homebrew/bin/git push -u origin csv-export"}}
{"name":"Bash","input":{"command":"gh auth status 2>&1"}}
```
Must fail:
```
Check `gh auth status`, then push each branch.
{"name":"Bash","input":{"command":"/opt/homebrew/bin/git push -u origin csv-export"}}
{"name":"Bash","input":{"command":"gh auth status 2>&1"}}
```
Must fail:
```
{"name":"Bash","input":{"command":"G=/opt/homebrew/bin/git; $G push origin csv-export"}}
```

### build/graders/shape-no-test-write.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/tests/test_export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":"toolu_01X","session_id":"s"}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/tests/test_export.py","content":"x"}}]},"parent_tool_use_id":"toolu_01X","session_id":"s"}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/orders/export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/tests/test_export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null,"session_id":"s"}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/tests/test_export.py","content":"x"}}]},"parent_tool_use_id":null,"session_id":"s"}
```

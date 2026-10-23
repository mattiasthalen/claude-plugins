# Grader samples — Intent

Offline samples for every regex shape grader in this scenario; `python3 evals/sdlc/tools/test_shape_graders.py` checks them. The `tool_used` graders' `input_match` patterns are not checked by it; their samples are kept here as documentation:

- `shape-no-write-outside-docs` / `shape-no-edit-outside-docs` `"file_path":\s*"(?![^"]*/sdlc(?:/|-(?!handoff/)))` matches (a violation) `"file_path": "/work/ordersdesk/orders/__main__.py"` and `"file_path": "/work/ordersdesk/sdlc-handoff/intent.md"`; it does not match `"file_path": "/var/folders/xy/T/sdlc-3f2a/intent.md"`.
- `shape-one-gh-issue-create` / `shape-no-gh-issue-create` `\bgh\s+issue\s+create\b` matches `{"command": "gh issue create --title \"Find a customer's orders\" --label story --body-file \"$TMPDIR/sdlc-3f2a/s2.md\""}`; it does not match `{"command": "gh auth status"}` or `{"command": "gh issue list --label story"}`.
- `shape-no-gh-issue` `\bgh\s+(?:issue\b|api\b[^\n]*\bissues\b)` matches `{"command": "gh issue view 42"}`, `{"command": "gh issue edit 42 --body-file x.md"}` and `{"command": "gh api repos/example/ordersdesk/issues -f title=x"}`; it does not match `{"command": "gh auth status"}` or `{"command": "git log --oneline"}`.
- `shape-interview-once` / `shape-interview-invoked` match a Skill call whose input holds `design-interview`, such as `{"skill": "design:design-interview"}`.

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

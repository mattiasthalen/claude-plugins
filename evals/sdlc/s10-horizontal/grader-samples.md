# Grader samples — S10

The `tool_used` graders' `input_match` patterns are not checked by `test_shape_graders.py`; their samples are kept here as documentation. `shape-no-write-outside-docs` / `shape-no-edit-outside-docs` pattern `"file_path":\s*"(?![^"]*/sdlc(?:/|-(?!handoff/)))` matches (a violation) `"file_path": "/work/ordersdesk/orders/export.py"` and `"file_path": "/work/ordersdesk/sdlc-handoff/spec.md"`; it does not match `"file_path": "/var/folders/xy/T/sdlc-3f2a/spec.md"` or `"file_path": "/private/tmp/claude-501/x/scratchpad/sdlc/plan.md"`.

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

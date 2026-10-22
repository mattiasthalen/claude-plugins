# Grader samples — Spec publishing

Offline samples for every regex shape grader in this scenario; `python3 evals/sdlc/tools/test_shape_graders.py` checks them. The `tool_used` graders' `input_match` patterns are not checked by it; their samples are kept here as documentation:

- `shape-one-gh-issue-create` `\bgh\s+issue\s+create\b` (min 1, max 1) matches `{"command": "gh issue create --title \"Spec: CSV export\" --label spec --body-file \"$TMPDIR/sdlc-3f2a/issue-body.md\""}`; it does not match `{"command": "gh issue view 7"}`.
- `shape-issue-body-no-run-path` `^(?!.*--body-file)(?!.*\s-F\s).*\bgh\s+issue\s+create\b.*sdlc[-/]` (max 0) matches (a violation) `{"command": "gh issue create --title \"Spec\" --body \"See $TMPDIR/sdlc-3f2a/spec.md. Refs #7\""}` and `{"command": "gh issue create --title Spec --body \"Spec at sdlc-handoff/spec.md\""}`; it does not match `{"command": "gh issue create --title Spec --body \"## Acceptance criteria\\n| C1 | … |\\nRefs #7\""}` or `{"command": "gh issue create --title Spec --body-file \"$TMPDIR/sdlc-3f2a/issue.md\""}` (a body file's content is judged by `content-issue-body-is-spec`).
- `shape-no-gh-issue` `\bgh\s+(?:issue\b|api\b[^\n]*\bissues\b)` (max 0) matches `{"command": "gh issue create --title x"}` and `{"command": "gh issue view 7"}`; it does not match `{"command": "gh auth status"}`.
- `shape-no-gh-issue-write` `\bgh\s+(?:issue\s+(?:create|edit|comment|close|reopen)\b|api\b[^\n]*\bissues\b)` (max 0) matches `{"command": "gh issue edit 8 --body-file x.md"}`, `{"command": "gh issue comment 8 --body \"Amended: C6\""}` and `{"command": "gh api -X PATCH repos/example/ordersdesk/issues/8 -f body=x"}`; it does not match `{"command": "gh issue view 8"}` or `{"command": "gh auth status"}`.

### docs-say/graders/shape-no-tracker-mcp.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"gh issue create --title Spec --body-file x.md"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/plan.md","content":"published on GitHub as #8"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__github__issue_write","input":{"method":"update","issue_number":8}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__Linear__save_issue","input":{"title":"Spec"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__Atlassian_MCP__editJiraIssue","input":{"issueIdOrKey":"OD-8"}}]},"parent_tool_use_id":null}
```

### silent/graders/shape-no-tracker-mcp.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"gh issue create --title Spec --body-file x.md"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/plan.md","content":"published on GitHub as #8"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__github__issue_write","input":{"method":"update","issue_number":8}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__Linear__save_issue","input":{"title":"Spec"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__Atlassian_MCP__editJiraIssue","input":{"issueIdOrKey":"OD-8"}}]},"parent_tool_use_id":null}
```

### amended/graders/shape-no-tracker-mcp.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"gh issue create --title Spec --body-file x.md"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/var/folders/xy/T/sdlc-3f2a/plan.md","content":"published on GitHub as #8"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__github__issue_write","input":{"method":"update","issue_number":8}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__Linear__save_issue","input":{"title":"Spec"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"mcp__Atlassian_MCP__editJiraIssue","input":{"issueIdOrKey":"OD-8"}}]},"parent_tool_use_id":null}
```

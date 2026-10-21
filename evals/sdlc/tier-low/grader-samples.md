# Grader samples — tier-low

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### build/graders/shape-security-pass.md
Must pass:
```
{"type":"tool_use","id":"toolu_1","name":"Skill","input":{"skill":"security-review"}}
```
Must pass:
```
{"type":"tool_use","id":"toolu_2","name":"Agent","input":{"description":"Security lens","prompt":"Review the diff for security issues","subagent_type":"general-purpose"}}
```
Must fail:
```
{"type":"tool_use","id":"toolu_3","name":"Agent","input":{"description":"Docs lens","prompt":"Check the README prose"}}
```
Must fail:
```
{"type":"text","text":"Skipping the security pass."}
```

### build/graders/shape-pr-body-file.md
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

### build/graders/shape-readme-edited.md
Must pass:
```
{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/README.md","content":"# ordersdesk"}}
```
Must pass:
```
{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/README.md","old_string":"a","new_string":"b"}}
```
Must fail:
```
{"type":"tool_use","id":"t1","name":"Read","input":{"file_path":"/w/README.md"}}
```
Must fail:
```
{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/docs/README.txt"}}
```

### build/graders/shape-build-before-pr.md
Must pass:
```
{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/README.md","content":"# ordersdesk"}}
{"type":"tool_use","id":"t2","name":"Bash","input":{"command":"gh auth status 2>&1"}}
```
Must pass:
```
{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/README.md","old_string":"a","new_string":"b"}}
{"type":"tool_use","id":"t2","name":"Bash","input":{"command":"gh auth status 2>&1"}}
```
Must fail:
```
{"type":"tool_use","id":"t2","name":"Bash","input":{"command":"gh auth status 2>&1"}}
{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/README.md","old_string":"a","new_string":"b"}}
```
Must fail:
```
{"type":"tool_use","id":"t1","name":"Read","input":{"file_path":"/w/README.md"}}
{"type":"tool_use","id":"t2","name":"Bash","input":{"command":"gh auth status 2>&1"}}
```

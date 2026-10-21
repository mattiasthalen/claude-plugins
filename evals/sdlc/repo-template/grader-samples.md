# Grader samples — repo template

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

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

### ship/graders/shape-template-read-before-body.md
Must pass:
```
{"command": "cat .github/pull_request_template.md"} {"file_path": "/T/sdlc-1/pr-csv-export.md", "content": "## What\n\n## Why\n\n## Verification\n"}
```
Must pass:
```
{"file_path": "/w/.github/pull_request_template.md"} {"file_path": "/T/sdlc-1/pr-csv-export.md", "content": "## Verification"}
```
Must fail:
```
{"file_path": "/T/sdlc-1/pr-csv-export.md", "content": "## Verification"} {"command": "cat .github/pull_request_template.md"}
```

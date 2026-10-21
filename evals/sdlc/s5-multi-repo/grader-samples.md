# Grader samples — s5-multi-repo

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### ship/graders/shape-two-prs.md
Must pass:
```
{"file_path": "/T/claude-501/sdlc-0000/api/pr-rename.md", "content": "## Summary"}
```
Must pass:
```
{"file_path": "/T/sdlc-0000/pr-rename.md", "content": "## Summary"}
```
Must fail:
```
{"file_path": "/w/api/pr-rename.md", "content": "## Summary"}
```

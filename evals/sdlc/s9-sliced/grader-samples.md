# Grader samples — S9 sliced

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### ship/graders/shape-slice2-stacked.md
Must pass:
```
gh pr create --base csv-export --head csv-export-since --title x --body-file y
```
Must pass:
```
gh pr create --base main --head csv-export --title x \\\n  --body-file a\n\ngh pr create -B csv-export --head csv-export-since
```
Must fail:
```
gh pr create --base main --head csv-export --title x
gh pr create --base main --head csv-export-since
```
Must fail:
```
gh pr create --base csv-export-since --head other
```

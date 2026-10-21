# Grader samples — review-seeded

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### review/graders/shape-source-fixed.md
Must pass:
```
        writer = csv.writer(f)
```
Must pass:
```
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL)
```
Must fail:
```
        f.write(",".join(fields) + "\r\n")
```
Must fail:
```
"""Writing the order book out as CSV for other systems."""
```

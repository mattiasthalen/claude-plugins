# Grader samples — S1

Offline samples for every regex shape grader in this scenario. `python3 evals/delivery/tools/test_shape_graders.py` checks them.

### plan/graders/shape-plan-has-guardrails.md
Must pass:
```
**Guardrails**
- G1 [7] — the existing suite passes
```
Must fail:
```
**Acceptance criteria**
- D1 [1] — export exits 0
```

### plan/graders/shape-plan-has-slices.md
Must pass:
```
## Slices
| Slice | Repo | Base | Direction | PR |
```
Must pass:
```
**Slices**: one vertical slice
```
Must fail:
```
We could slice this vertically later.
```

### plan/graders/shape-plan-has-capture.md
Must pass:
```
## Capture (after approval)
- ADR-0001 — export writes RFC 4180 CSV
```
Must fail:
```
Nothing to capture yet; the brief covers it.
```

### plan/graders/shape-plan-has-progress.md
Must pass:
```
## Progress
- [ ] Capture
- [ ] Build S1
```
Must fail:
```
## Progress
Capture, build, review, evidence, PR.
```

### build/graders/shape-page-lists-every-criterion.md
Must pass:
```
<td>D1</td><td>✘</td><td>✔</td> D2 D3 E1 E2 E3 E4 G1
```
Must fail:
```
<td>D1</td><td>✔</td> D2 D3 E1 E2 E3 G1
```
Must fail:
```
D1 D2 D3 E1 E2 E3 E4 G1 all done
```

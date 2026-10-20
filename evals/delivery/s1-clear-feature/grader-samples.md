# Grader samples — S1

Offline samples for every regex shape grader in this scenario. `python3 evals/delivery/tools/test_shape_graders.py` checks them.

### plan/graders/shape-plan-has-guardrails.md
Must pass:
```
**Guardrail:** `orders list` output unchanged
```
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
Must pass:
```
## 3. Slices
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

### pr/graders/shape-sections-in-order.md
Must pass:
```
## Summary
x
## Brief
y
## Evidence
z
## Merge Danger
w
```
Must fail:
```
## Summary
## Evidence
## Merge Danger
```

### pr/graders/shape-one-details.md
Must pass:
```
## Brief
One line.
<details><summary>Full brief</summary>...</details>
```
Must fail:
```
<details>a</details>
<details>b</details>
```
Must fail:
```
## Brief
The full brief, inline.
```

### pr/graders/shape-no-images.md
Must pass:
```
## Evidence
| D1 | ✘ | ✔ |
```
Must fail:
```
![screenshot](shot.png)
```

### pr/graders/shape-no-page-link.md
Must pass:
```
## Evidence
condensed rows
```
Must fail:
```
Full evidence: https://claude.ai/code/artifact/abc
```

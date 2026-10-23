# S3 — Sizing

Two ends of size (A18, ported from `delivery`). An epic of four independent features goes through the intent stage: `intent.md` holds one story per part and the intent gate asks what happens to each (now / file / drop). A tiny change, handed in as an `intent.md` with the requester saying it needs no interview, skips the interview, but still gets a spec with checks and a preservation criterion, and still stops at the spec gate.

**Fixture:** `ordersdesk`.

| Case | Starts from | Graded |
|---|---|---|
| `epic` | a four-part intent, fresh | `intent.md` in the run folder with a story per part; stops at the intent gate asking dispositions; no `design-interview`, no spec, no repo writes |
| `small` | `/sdlc continue from spec using sdlc-handoff/intent.md` (the `--version` story, laid in by the scaffold, git-excluded) and "tiny, no interview needed" | no interview; `spec.md` in the docs dir with checks and a preservation criterion; no plan, no repo writes, no test-writer; stops at the spec gate with the seam choice |

# Resume

`/sdlc continue from <stage> using <paths>` (A6). The documents are the only state: with a valid spec the run starts at the plan stage without rerunning the interview; with a path that does not exist it refuses and asks for the document.

**Fixture:** `ordersdesk`. `from-plan` lays the S1 spec (`from-plan/handoff/spec.md`, the CSV export) into `sdlc-handoff/`, uncommitted.

| Case | Prompt | Graded |
|---|---|---|
| `from-plan` | `/sdlc continue from plan using sdlc-handoff/spec.md` | no `design-interview`; `plan.md` written in the docs dir, built on the spec's ids; spec not rewritten; no repo writes, no test-writer; stops at the plan gate |
| `missing` | `/sdlc continue from plan using sdlc-handoff/missing.md` | no `design-interview`; no `plan.md` or `spec.md`; no repo writes; refuses and asks for the document |

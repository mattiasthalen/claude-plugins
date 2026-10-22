# Resume

`/sdlc continue from <stage> using <paths>` (A6). The documents are the only state: with a valid spec the run starts at the plan stage without rerunning the interview; with a path that does not exist it refuses and asks for the document.

**Fixture:** `ordersdesk`. `from-plan` lays the S1 spec (`from-plan/handoff/spec.md`, the CSV export) into `sdlc-handoff/`, uncommitted. `epic-spec` lays `back-office.md`, the four-part revamp as meeting notes with no stories, into `sdlc-handoff/`, git-excluded.

| Case | Prompt | Graded |
|---|---|---|
| `from-plan` | `/sdlc continue from plan using sdlc-handoff/spec.md` | no `design-interview`; `plan.md` written in the docs dir, built on the spec's ids; spec not rewritten; no repo writes, no test-writer; stops at the plan gate |
| `missing` | `/sdlc continue from plan using sdlc-handoff/missing.md` | no `design-interview`; no `plan.md` or `spec.md`; no repo writes; refuses and asks for the document |
| `epic-spec` (E3) | `/sdlc continue from spec using sdlc-handoff/back-office.md` | spec's backstop for a document with several changes and no stories: names the parts, asks which; no `design-interview`, no `spec.md`, no repo writes |

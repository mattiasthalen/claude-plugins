# ADR-0016 — Design capture is staged in the run's folder and committed by build

**Status:** Accepted (2026-11-01)

## Context

`sdlc`'s spec stage runs `design:design-interview`, whose capture writes the design's durable records (ADRs, the lexicon, the assumptions record) beside the project's design documentation, and the feature's brief where the build reads it. The interview captures only on request; `sdlc` stopped it at its wrap-up, so the records were lost with the session. Until the plan is approved, the stage hook ([ADR-0009](0009-tests-are-written-and-approved-before-the-build-and-only-by-the-test-writer.md)) refuses every write outside the run's folder. [ADR-0008](0008-sdlc-keeps-spec-plan-and-evidence-in-the-session-scratchpad.md) keeps `sdlc`'s own documents out of the repo. The design skills' rules decide what is captured and where it belongs, and `sdlc` must not override them.

## Decision

The spec stage's invocation of the interview is the request for capture, so capture always runs. Capture writes under `capture/<repo>/` in the run's folder, named for the repository each record belongs to, at the repo-relative path the interview chose: from the design documentation its scan found, or by asking the requester once where there is none. The brief goes to `capture/brief/` and is never committed: the build reads the run's folder. On the first slice in a repo, build's first commit, before any code, copies that repo's `capture/<repo>/` to the same paths in the repo, and nothing else. A run without `capture/` makes no capture commit.

Rejected:
- Letting the spec stage write the project's `docs/`: a write into the repo before the plan is approved.
- A flat `capture/` folder whose files build places: build would re-decide where the design skills put each record.
- Repo-relative paths directly under `capture/`: a multi-repo run could not tell which repo a record belongs to.
- Committing capture last, after the code: the decision lands after the change it explains.
- A separate pull request for the records: it splits a decision from its change and can merge without it.

## Consequences

- ADRs, the lexicon and the assumptions record reach the repo with the change they describe; the spec, plan, evidence and brief still do not.
- The records are approved with the spec and plan before any of them is written into the repo.
- Build copies whole files. A record changed on the base between the spec gate and build is overwritten by the copy; detecting that is left for later.

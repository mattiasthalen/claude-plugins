# Decisions

Architecture decision records for this marketplace, in Michael Nygard's format. Records from before the 2026-11-10 rebuild are in git history and are not continued here.

## Index

| ADR | Title | Status |
|-----|-------|--------|
| [0001](0001-sdlc-is-a-flow-skill-and-an-intent-skill-that-delegate-every-step.md) | sdlc is a flow skill and an intent skill that delegate every step | Accepted |
| [0002](0002-upstream-plugins-follow-their-default-branch-unpinned-and-uncopied.md) | Upstream plugins follow their default branch, unpinned and uncopied | Accepted |
| [0003](0003-working-documents-stay-out-of-the-repository.md) | Working documents stay out of the repository; only ADRs, assumptions and the lexicon are committed | Accepted |

## Conventions

- This index is the canonical list of ADRs; keep it in step with the files.
- Filenames: `NNNN-kebab-case-title.md`, numbered sequentially.
- An ADR records one decision that is architecturally significant and hard to change later.
- Status is one of: Proposed, Accepted, Rejected, Deprecated, Superseded.
- An Accepted ADR's body is never rewritten. A new ADR supersedes it when the decision is overturned or changes in substance; anything else is appended as a dated addendum.

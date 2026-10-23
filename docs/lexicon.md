# Lexicon

The words someone needs defined to talk about using or developing this marketplace's plugins. A term earns an entry only if it is language rather than code, needs defining beyond its ordinary meaning, and is the one word for its concept.

**check** — A pass/fail verdict on one criterion or edge case of a *spec*: executable (a command and its exit code) or judged (a fresh-context reviewer's verdict against a rubric fixed before the build, always flagged as judged).

**delivery** — One change, one or several of the *intent*'s stories, taken from the *intent* through *spec*, *plan*, tests, build, review and *evidence* to pull requests. Distinct from a *slice*, an increment within it, and from an epic, an *intent* of several stories.

**evidence** — Each criterion's *check* result at a *slice*'s head, with CI and the existing suite, review dispositions, assumptions and risk: what the evidence *gate* shows and each pull request's Testing section carries. It shows that what was asked for is done and nothing known broke, never that nothing broke. "Proof" is not used. See [ADR-0009](decisions/0009-tests-are-written-and-approved-before-the-build-and-only-by-the-test-writer.md).

**gate** — A *seam* where the requester approves a document before the *delivery* goes on: the *intent*, the *spec*, the *plan*, the tests, the *evidence*. Every gate is a *seam*.

**intent** — The why of a run, and of each *delivery* in it: the request as it arrives, whether a ticket, free text or a file, written by the intent stage as user stories in `intent.md` (id, As a / I want / So that, acceptance criteria, notes). Distinct from the *spec*, which says what must be true. See [ADR-0015](decisions/0015-every-fresh-sdlc-run-starts-with-an-intent-stage-that-writes-user-stories.md). "Pitch" is not used.

**plan** — The how of a *delivery*: its *slices*, their order, and what each *check* will verify. Distinct from the *spec*, the what, and from plan mode, which `sdlc` does not use.

**preservation criterion** — An acceptance criterion that something must not change: its *check* passes at the base and must still pass at the head. Distinct from a change criterion, whose check fails at the base. "Guardrail" is not used.

**seam** — A point where the run hands control back to the requester, at a *gate* or an early stop, and asks whether to continue in this session, continue in a new one, or stop.

**slice** — An increment of a *delivery*, with its own part of the *spec*, *checks*, branch and pull request, that ships on its own and leaves the system consistent. Distinct from a step, which ships nothing by itself.

**spec** — What a *delivery* is held to: its acceptance criteria, *preservation criteria* among them, and edge cases, each with a *check* and the design branch it came from. Distinct from the *plan*, and from the design interview's capture, which has no checks. "Brief" is not used.

**tier** — Risk, Low, Medium or High, by what going wrong would cost. A change's tier is set by the paths it touches and decides how deep review goes and whether the evidence *gate* stops; an eval case's tier is set by the behaviour it guards and decides how many runs it gets. See [ADR-0011](decisions/0011-risk-tiers-are-set-by-changed-paths-in-review-md-frontmatter.md).

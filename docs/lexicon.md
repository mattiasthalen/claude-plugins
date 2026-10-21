# Lexicon

The words someone needs defined to talk about using or developing this marketplace's plugins. A term earns an entry only if it is language rather than code, needs defining beyond its ordinary meaning, and is the one word for its concept.

**check** — A pass/fail verdict on one criterion or edge case of a *spec*: executable (a command and its exit code) or judged (a fresh-context reviewer's verdict against a rubric fixed before the build, always flagged as judged).

**delivery** — One change taken from an *intent* through *spec*, *plan*, tests, build, review and *evidence* to pull requests. Distinct from a *slice*, an increment within it, and from an epic, which is several deliveries.

**evidence** — Each criterion's *check* result at a *slice*'s head, with CI and the existing suite, review dispositions, assumptions and risk: what the evidence *gate* shows and each pull request's Testing section carries. It shows that what was asked for is done and nothing known broke, never that nothing broke. "Proof" is not used. See [ADR-0009](decisions/0009-tests-are-written-and-approved-before-the-build-and-only-by-the-test-writer.md).

**gate** — A *seam* where the requester approves a document before the *delivery* goes on: the *spec*, the *plan*, the tests, the *evidence*. Distinct from a seam that only asks whether to proceed.

**intent** — The why of a *delivery*: the request as it arrives, whether a ticket, free text or a file. Distinct from the *spec*, which says what must be true. "Pitch" is not used.

**plan** — The how of a *delivery*: its *slices*, their order, and what each *check* will verify. Distinct from the *spec*, the what, and from plan mode, which `sdlc` does not use.

**preservation criterion** — An acceptance criterion that something must not change: its *check* passes at the base and must still pass at the head. Distinct from a change criterion, whose check fails at the base. "Guardrail" is not used.

**seam** — A boundary between two stages of a *delivery*, where the requester chooses to continue in this session, continue in a new one, or stop. Every *gate* is a seam; not every seam is a gate.

**slice** — An increment of a *delivery*, with its own part of the *spec*, *checks*, branch and pull request, that ships on its own and leaves the system consistent. Distinct from a step, which ships nothing by itself.

**spec** — What a *delivery* is held to: its acceptance criteria, *preservation criteria* among them, and edge cases, each with a *check* and the design branch it came from. Distinct from the *plan*, and from the design interview's capture, which has no checks. "Brief" is not used.

**tier** — A change's risk, Low, Medium or High, set by the paths it touches; it decides how deep review goes and whether the evidence *gate* stops for the requester. See [ADR-0011](decisions/0011-risk-tiers-are-set-by-changed-paths-in-review-md-frontmatter.md).

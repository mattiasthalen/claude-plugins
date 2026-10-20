# Lexicon

The words someone needs defined to talk about using or developing this marketplace's plugins. A term earns an entry only if it is language rather than code, needs defining beyond its ordinary meaning, and is the one word for its concept.

**brief** — What a *delivery* is held to: the design's spec, edge cases, acceptance criteria and *guardrails*, each with a *check* and the design branch it came from. Distinct from the plan, which also carries the design tree, and from the exodus design-interview's brief, which has no guardrails.

**check** — A pass/fail verdict on one criterion, edge case or *guardrail*: executable (a command and its exit code) or judged (a fresh-context reviewer's verdict, always flagged as judged).

**delivery** — One feature taken from a pitch through design, plan, build, *evidence* and pull requests. Distinct from a *slice*, an increment within it, and from an epic, which is several deliveries.

**evidence** — Each *check*'s result at a *slice*'s base and head (a judged check at the head only), with guardrail mutants, review dispositions, assumptions and merge danger: the one source the *gate* reply, the evidence page and the pull request bodies render. Spent once approved. "Proof" is not used. See [ADR-0002](decisions/0002-evidence-baseline-is-recomputed-by-overlaying-checks-on-the-base.md).

**gate** — The point where the requester approves the *evidence*; pull requests open only after it. Distinct from plan approval, which gates the build.

**guardrail** — Something the *brief* says must not change, decided by a *check* that passes both before and after the change. Distinct from an acceptance criterion, whose check must fail before and pass after.

**slice** — An increment of a *delivery*, with its own part of the *brief*, *checks*, branch and pull request, that ships on its own and leaves the system consistent. Distinct from a step, which ships nothing by itself.

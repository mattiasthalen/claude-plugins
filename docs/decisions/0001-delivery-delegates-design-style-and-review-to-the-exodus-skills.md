# ADR-0001 — delivery delegates design, style and review to the exodus skills by dependency

**Status:** Superseded by [ADR-0007](0007-one-model-invocable-sdlc-skill-loads-a-reference-file-per-stage.md) (2026-10-21)

## Context

`delivery` takes one feature from a pitch to ready pull requests. Its predecessor, pitch-and-deliver, grew its own interview, brief and review loop because its ADR-0005 forbade delegating to Tobias Karlsson's the-exodus/claude-design-skills: an ablation arm could not remove content held in another plugin. Keeping parity with exodus by hand became the main cost: its interview "fell well short of exodus's design-interview", and every line had to be re-earned.

Upstream ships two plugins: `design` (design-interview, design-philosophy, adr, lexicon) and `implementation` (code-style, review-cycle; depends on `design >=0.7.0`). Neither builds, proves or opens pull requests; review-cycle ends by handing back to a PR step it does not define. Upstream releases often (design 0.5 → 0.8 in a month; review-cycle at 0.1.0) and its skills call each other by qualified name (`design:adr`, `design:lexicon`).

## Decision

`delivery` lists `design` and `implementation` in this marketplace as `git-subdir` entries on upstream's default branch and declares both in `dependencies`. Its skill invokes them by qualified name and never copies their text. It owns only what upstream lacks: the plan's shape with guardrails, slicing, the evidence gate, and pull request creation.

Rejected:
- An interview and review of its own, as pitch-and-deliver has: it re-creates upstream at a permanent maintenance cost, the reason pitch-and-deliver is being replaced.
- Vendoring upstream's skills: copied under `delivery`, their `design:*` cross-references point at nothing, and the copies freeze skills that change weekly.
- Four skills (an entry chaining `building-slices`, `proving-changes`, `shipping-prs`), all with `disable-model-invocation`: Claude Code blocks Claude from invoking a disabled skill and from reproducing its steps another way, so the entry cannot chain them. One skill holds every stage until real standalone use or an eval earns a split.

## Consequences

- An upstream release can change `delivery`'s behaviour with no change here; a broken hand-off shows up as a failing eval (assumption A2).
- Ablation measures `delivery`'s own lines only. Upstream's behaviour is upstream's suite's concern.
- Installing `delivery` installs both upstream plugins, with all their model-invocable skills.

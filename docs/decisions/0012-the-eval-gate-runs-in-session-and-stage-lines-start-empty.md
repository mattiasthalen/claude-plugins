# ADR-0012 — The eval gate runs in-session, and stage lines start empty

**Status:** Accepted (2026-10-21) · **Supersedes:** [ADR-0004](0004-skill-lines-are-earned-by-evals-and-ablation.md)

## Context

ADR-0004 had `delivering-pitches` start empty, admit a line only when a case failed without it, and keep it only if deleting it dropped a grader below its bar; the deletion pass cost about $1.5k and was stopped part way. The playbook runs evals in CI whenever a skill, `CLAUDE.md` or a hook changes. Running them in GitHub Actions needs a Claude API token in the repository, which the requester will not add. `sdlc` is mostly an orchestrator, so its failures are sequencing failures: a skipped gate, a stage run twice, a resume that reruns the interview.

## Decision

Each `sdlc` stage file starts empty, and a line enters only when a case in `evals/sdlc/` fails without it. Every case grades sequence — which stage ran, what it read, where it stopped — not only output. Each case carries a tier, set by what a failure of the behaviour it guards would cost, and the tier sets its runs in `prompt.md`: High — something outward or irreversible, such as a pull request before approval, repo writes before the plan is approved, the builder editing tests, `sdlc` firing on an unrelated conversation — runs eight times and must pass all; Medium — a broken sequence, such as a gate that does not stop or a resume at the wrong stage — runs three times, deterministic graders 3/3 and judged 2/3; Low — wording and presentation — runs once. While lines are being earned every case runs once. Agent and judge pinned to `claude-opus-5-5`; spend uncapped. CI stays tokenless and deterministic: `claude plugin validate --strict`, the offline grader tests and the hook's unit tests. The eval pass-rate gate runs in-session, in the prove stage, whenever a skill, agent, `CLAUDE.md` or hook changes; below bar, no pull request opens. The deletion pass is deferred until context cost or a suspected dead line calls for it.

Rejected:
- An eval gate in CI: needs a Claude API token.
- Writing the skill first and ablating: lines nobody needs stay in forever.
- The same runs for every case (ADR-0004's five): spends as much on a wording check as on the gate before a pull request.

## Consequences

- A merged change's eval results live in its pull request's Testing section, not in a CI run.
- Lines may carry unneeded text until a deletion pass runs.
- Every skill change still rebuilds histories and reruns the affected cases.

# ADR-0003 — Working documents stay out of the repository; only ADRs, assumptions and the lexicon are committed

**Status:** Accepted (2026-11-10)

## Context

A change produces two kinds of document. Some describe the system and stay true across changes: the decision records, the assumptions record and the lexicon. Others are spent when the change ships: the intent's stories, the design interview's brief (functional spec, edge cases, acceptance criteria), and the proof. The project-thread Library exists only in claude.ai project threads, not in the local CLI.

## Decision

Only ADRs, the assumptions record and the lexicon are committed. A change's working documents live in the session scratchpad, in one folder per change: `sdlc/<change>/`, holding `stories.md` and the brief. A story reaches a tracker only when Mattias asks for it.

Rejected:

- **Committing the stories and brief beside the docs:** they describe one change, go stale the moment it ships, and the next design interview would read them as if they described the system.
- **The project Library when there is one, else the scratchpad:** two locations for the skill to handle, and it helps only in project threads.
- **No file at all, stories only in the conversation:** the coverage check and the proof come after a long interview, and losing context loses the stories.

## Consequences

- The working documents die with the session. The proof artifact is where the stories and criteria are seen after that.
- A later session cannot resume a change from its documents unless it is handed them.

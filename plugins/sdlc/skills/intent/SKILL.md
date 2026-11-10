---
name: intent
description: Step 1 of the sdlc flow. Load only when the sdlc skill reaches its intent step, or when asked to run /sdlc:intent.
---

1. **Why first.** Until you know why I want this, ask one open question at a time about the problem, with no options to pick from.
2. **Stories.** Write them to `sdlc/<change>/stories.md` in the session scratchpad: the why, the non-goals, then each story as "As a … I want … so that …" with acceptance criteria and a disposition, now, later or drop. Mark every criterion [stated] if I said it, or [proposed] with why you added it.
3. **Filing.** When I approve the stories, ask once whether any should be filed on a tracker. File only the ones I name, where I say. A failed filing stops the hand-off: tell me which story failed and why, and wait for my call.
4. **Hand-off.** Run `/design:design-interview` with the now stories, the why and the non-goals as its arguments, saying that [stated] criteria are requirements and that later and dropped stories are out of scope.

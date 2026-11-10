---
name: sdlc
description: Load first, before any design, test or code, whenever asked to implement, add, fix or change behaviour in a repo. Sets the order every change runs in, from user stories to pull request.
---

Every change I ask for runs these steps in order. Size is my call, never yours: when I say the change is small, start at step 3; otherwise start at step 1 without asking.

1. **Intent.** Run `/sdlc:intent`. It hands off to `/design:design-interview`, which runs to its end and writes its capture.
2. **Coverage.** Check every [stated] criterion in the stories against the brief's acceptance criteria. Done when each is covered, or I've decided what to do about each one that isn't.
3. **Tests first.** Load `/design:design-philosophy` and `/implementation:code-style`, plan the slices, and write a test for every acceptance criterion. Done when each test is red and committed before any code.
4. **SHOW ME.** After build and review, show the proof: each acceptance criterion going red to green, the full local suite at the head, each review finding and its outcome, and every change to an existing test. Then wait for my go.
5. **PR.** On my go, open the pull request with `/mattpocock-skills:pr`.
6. **Retro.** When I say it's merged, remind me to run `/mattpocock-skills:retro`.

# Test

Dispatch the `sdlc:test-writer` agent with `spec.md` and the plan's check descriptions, and only those. It writes every test and judged rubric and commits them on the slice's branch.

Then run every check at the base and show each result by id: a change criterion should be red, a preservation criterion green. Flag every other result; a change criterion already green means the work may be done already, so ask the requester before going on.

End at the test gate. Say that the next stretch — build, review, prove — runs unattended, and recommend auto mode or allowed tools for the build's commands so it does not wait on prompts.

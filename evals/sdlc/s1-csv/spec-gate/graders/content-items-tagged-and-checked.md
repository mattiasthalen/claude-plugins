---
type: llm
focus: trace
---

Judge one thing only, on the spec.md the run wrote into its docs dir (`…/sdlc-…/spec.md`; read the content of the Write call or Bash command that created it): does every acceptance criterion, preservation criterion and edge case carry the design branch it comes from and a check?

PASS if each item names a branch number from the tree in the conversation (1–8, or a branch the spec adds and marks as its own) and a check: a command, a named test, or one marked as judged.

FAIL if no spec.md was written, if any item lacks a branch tag or a check, or a check is only "verify manually" with nothing named.

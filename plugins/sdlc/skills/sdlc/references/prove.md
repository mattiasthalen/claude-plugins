# Prove

Trust nothing the build reported. At each slice's head, run every check, the repository's existing tests and CI's commands. Run `git diff <test gate commit>..HEAD` over the test paths: a change there outside the test-writer's commits voids the evidence. Where the diff touches a skill, agent, `CLAUDE.md` or hook and the repo has eval suites, run the affected suites with `claude plugin eval` and report their pass rates.

Write `evidence.md`:

- the claim: what was asked for, and what is true now;
- per slice, base and head SHAs and a table of every criterion and edge case: check, result at the head;
- the existing suite and CI at the head;
- tests added mid-run, marked as such, each with the review finding it came from;
- review: rounds used, findings by disposition, what was closed with a reason;
- tier, merge danger (a one- or two-way door, and the blast radius), assumptions, follow-ups.

A criterion red, the existing suite or CI red, an open bug or security finding, or an eval below its bar: no pull request. Lead the evidence with it — its last output, what was tried, why it fails — and offer continue (another try, checks unchanged), re-plan (amend the spec or plan; a wrong check goes here) or abandon. Never call it done.

Otherwise, at Low tier go straight to ship, and say in the final reply that Low tier, and the paths that made it so, is why no evidence gate was asked. At Medium, end at the evidence gate; at High, say which path made it High, and ask the requester to read the diff, not only the evidence. Where the Artifact tool exists, also publish `evidence.md` as a page.

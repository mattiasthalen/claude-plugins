# Plan

Read `spec.md`, then write `plan.md`:

- **Slices**: a table of slice, repo, base, direction and pull request. Every slice ships on its own and leaves the system consistent. Cut vertically by default; cut horizontally, or keep one slice, when a per-feature cut would leave a mixed state, such as a storage swap. Say which, and why.
- **Checks**: for every criterion and edge case by its id, what its check will verify and where it will live. The test stage writes them; the plan names them.
- **Order**: the build order within each slice, and the risks.

Write no tests and no code. End at the plan gate.

---
# The list exists before step 1 starts, so the run is followable from its first step.
type: tool_order
before: TaskCreate
after: { tool: Skill, input_match: '"skill"\s*:\s*"(?:design:)?design-interview"' }
---

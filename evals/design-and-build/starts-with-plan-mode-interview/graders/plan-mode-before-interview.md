---
# Plan mode is entered before the interview starts, so the whole interview runs inside it.
type: tool_order
before: EnterPlanMode
after: { tool: Skill, input_match: '"skill"\s*:\s*"(?:design:)?design-interview"' }
---

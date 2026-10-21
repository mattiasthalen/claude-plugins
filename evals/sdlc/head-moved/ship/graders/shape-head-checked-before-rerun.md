---
type: tool_order
before: {tool: Bash, input_match: 'git[^\n]*\s(rev-parse|log|status)\b'}
after: {tool: Bash, input_match: 'unittest'}
---

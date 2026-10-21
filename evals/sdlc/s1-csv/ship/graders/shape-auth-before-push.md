---
type: tool_order
before: {tool: Bash, input_match: 'gh auth status'}
after: {tool: Bash, input_match: 'git[^\n]*\spush\b'}
---

---
type: tool_order
before: {tool: Edit, input_match: '"file_path":\s*"[^"]*/orders/'}
after: {tool: Bash, input_match: '\bgit\b.*\bdiff\b.*\s--\s.*test'}
---

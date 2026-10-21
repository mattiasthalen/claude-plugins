---
type: tool_order
before: {tool: Edit, input_match: '"file_path":\s*"[^"]*/README\.md"'}
after: {tool: Bash, input_match: 'gh (auth status|pr create)'}
---

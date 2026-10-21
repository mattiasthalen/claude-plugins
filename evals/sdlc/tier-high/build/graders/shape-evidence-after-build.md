---
type: tool_order
before: {tool: Edit, input_match: '"file_path":\s*"[^"]*/\.github/workflows/ci\.yml"'}
after: {tool: Write, input_match: '"file_path":\s*"[^"]*/sdlc[-/][^"]*evidence\.md"'}
---

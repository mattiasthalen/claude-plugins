---
type: tool_order
before: {tool: Agent, input_match: '^(?!.*"subagent_type":\s*"sdlc:test-writer")'}
after: {tool: Agent, input_match: '"subagent_type":\s*"sdlc:test-writer"'}
---

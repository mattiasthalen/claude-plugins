---
type: tool_used
tool: Write
input_match: '"file_path":\s*"[^"]*/pr-[^"]*\.md"(?=[\s\S]*##\s+Summary)(?=[\s\S]*##\s+Testing(?=(?:(?!##\s)[\s\S])*\bC1\b)(?=(?:(?!##\s)[\s\S])*\bC2\b)(?=(?:(?!##\s)[\s\S])*\bP1\b)(?=(?:(?!##\s)[\s\S])*\bP2\b))(?=[\s\S]*##\s+Risk)(?=[\s\S]*##\s+How to revert)'
min: 1
---

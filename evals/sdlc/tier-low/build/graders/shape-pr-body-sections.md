---
type: tool_used
tool: Write
input_match: '"file_path":\s*"[^"]*/pr-[^"]*\.md"(?=[\s\S]*##\s+Summary)(?=[\s\S]*##\s+Testing(?=(?:(?!(?:\\n|\n)##\s)[\s\S])*\bC1\b)(?=(?:(?!(?:\\n|\n)##\s)[\s\S])*\bC2\b)(?=(?:(?!(?:\\n|\n)##\s)[\s\S])*\bP1\b)(?=(?:(?!(?:\\n|\n)##\s)[\s\S])*\bP2\b))(?=[\s\S]*##\s+Risk)(?=[\s\S]*##\s+How to revert)'
min: 1
---

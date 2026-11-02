---
type: regex
target: trace
match: not_contains
pattern: '"name":\s*"Write",\s*"input":\s*\{\s*"file_path":\s*"[^"]*/spec\.md"|"name":\s*"Bash",\s*"input":\s*\{\s*"command":\s*"(?:[^"\\]|\\.)*?(?:(?<![0-9&])>>?|\btee\s+(?:-a\s+)?)\s*(?:\\"|'')?[^\s"''\\]*spec\.md\b|"name":\s*"Bash",\s*"input":\s*\{\s*"command":\s*"(?:[^"\\]|\\.)*?\b(?:cp|mv)\s(?:[^"\;&|]|\\.)*?\s(?:\\"|'')?[^\s"''\\]*spec\.md(?:\\"|'')?\s*(?="|;|&|\||\\n)'
---

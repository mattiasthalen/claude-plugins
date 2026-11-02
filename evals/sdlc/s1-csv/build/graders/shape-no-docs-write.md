---
type: regex
target: trace
match: not_contains
pattern: '"name":\s*"(?:Write|Edit)",\s*"input":\s*\{\s*(?:"replace_all":\s*(?:true|false),\s*)?"file_path":\s*"(?![^"]*/sdlc[-/])[^"]*/docs/|"name":\s*"Bash",\s*"input":\s*\{\s*"command":\s*"(?:[^"\\]|\\.)*?(?:(?<![0-9&])>>?|\btee\s+(?:-a\s+)?|\bmkdir\s+(?:-p\s+)?)\s*(?:\\"|'')?(?![^\s"''\\]*/sdlc[-/])(?:[^\s"''\\]*/)?docs(?:/|\b)|"name":\s*"Bash",\s*"input":\s*\{\s*"command":\s*"(?:[^"\\]|\\.)*?\b(?:cp|mv|rsync)\s(?:[^";&|]|\\.)*?\s(?:\\"|'')?(?![^\s"''\\]*/sdlc[-/])(?:[^\s"''\\]*/)?docs/?(?:\\"|'')?\s*(?="|;|&|\||\\n)'
---

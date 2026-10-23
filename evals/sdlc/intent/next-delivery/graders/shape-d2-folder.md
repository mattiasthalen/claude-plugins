---
type: regex
target: trace
pattern: '"name":"(?:Write|Edit)","input":\{(?:"replace_all":(?:true|false),)?"file_path":"[^"]*/sdlc(?:-(?!handoff/)[^"/]*)?/(?:[^"]*/)?d2/|"name":"Bash","input":\{"command":"(?:[^"\\]|\\.)*?(?:\bmkdir\b|>|\btee\b|\bcp\b|\bmv\b)(?:[^"\\]|\\.)*?/sdlc(?:-(?!handoff/)[^\s"''\\/]*)?/(?:[^\s"''\\]*/)?d2\b'
---

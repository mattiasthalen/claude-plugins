---
type: regex
target: trace
pattern: '^(?:(?!"name":\s*"(?:Write|Edit)",\s*"input":\s*\{\s*(?:"replace_all":\s*(?:true|false),\s*)?"file_path":\s*"[^"]*/orders/|"name":\s*"Bash",\s*"input":\s*\{\s*"command\\?":\s*\\?"(?:[^"\\]|\\.)*?(?:(?<![0-9&<>])>>?|\btee\s+(?:-a\s+)?)\s*(?:\\+"|'')?(?:[^\s"''\\&|;<>()]*/)?orders/[^\s"''\\&|;<>()]+)[\s\S])*?(?:"name":\s*"Write",\s*"input":\s*\{\s*"file_path":\s*"(?![^"]*/capture/)(?![^"]*/sdlc[-/])[^"]*/docs/decisions/0001-the-csv-export-follows-rfc-4180\.md"|"name":\s*"Bash",\s*"input":\s*\{\s*"command":\s*"(?=(?:[^"\\]|\\.)*?\b(?:cp|rsync|ditto)\s)(?:[^"\\]|\\.)*?capture/ordersdesk\b)'
---

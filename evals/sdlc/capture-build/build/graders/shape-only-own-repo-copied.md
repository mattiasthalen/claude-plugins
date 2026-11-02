---
type: regex
target: trace
match: not_contains
pattern: '"name":\s*"(?:Write|Edit)",\s*"input":\s*\{\s*(?:"replace_all":\s*(?:true|false),\s*)?"file_path":\s*"(?![^"]*/capture/)(?![^"]*/sdlc[-/])[^"]*/(?:docs/x\.md|ledger/)|"name":\s*"Bash",\s*"input":\s*\{\s*"command\\?":\s*\\?"(?:[^"\\]|\\.)*?(?:(?<![\w-])|(?<=\\[nr]))(?:cp|mv|rsync|ditto)\s(?:[^"\\&|;#\n\r]|\\[^nr])*?(?:(?<![\w.-])capture/(?!ordersdesk\b)|(?<![\w.-])capture(?=\\*["'']|[\s;&|]))|"name":\s*"Bash",\s*"input":\s*\{\s*"command":\s*"(?:[^"\\]|\\.)*?(?<![0-9&])>>?\s*(?:\\"|'')?(?![^\s"''\\]*/capture/)(?:[^\s"''\\]*/)?docs/x\.md'
---

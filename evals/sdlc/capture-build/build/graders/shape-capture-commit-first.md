---
type: regex
target: trace
pattern: '^(?:(?!"name":\s*"(?:Write|Edit)",\s*"input":\s*\{\s*(?:"replace_all":\s*(?:true|false),\s*)?"file_path":\s*"[^"]*/orders/)[\s\S])*?(?:"command":\s*"(?=(?:[^"\\]|\\.)*?\bdocs\b)(?:[^"\\]|\\.)*?(?:\bgit|\$\{?G(?:IT)?\}?)(?:\s+-[cC]\s+\S+)*\s+commit\b|"command":\s*"(?:[^"\\]|\\.)*?(?:\bgit|\$\{?G(?:IT)?\}?)(?:\s+-[cC]\s+\S+)*\s+add\s(?:[^"\\;&|]|\\.)*?(?:\bdocs\b|(?<!\S)(?:-A|--all|\.)(?!\S))(?:(?:[^"\\]|\\.)*?|(?:(?!"name":\s*"(?:Write|Edit)",\s*"input":\s*\{\s*(?:"replace_all":\s*(?:true|false),\s*)?"file_path":\s*"[^"]*/orders/)[\s\S])*?"command":\s*"(?:[^"\\]|\\.)*?)(?:\bgit|\$\{?G(?:IT)?\}?)(?:\s+-[cC]\s+\S+)*\s+commit\b)'
---

---
type: regex
target: trace
pattern: '(?:file_path\\?"\s*:\s*\\?"|\b(?:cat|head|sed)\s[^\n]*?)[^\s"\\]*\.github/pull_request_template\.md[\s\S]*?/pr-[\w.-]+\.md[\s\S]{0,3000}?##\s+Verification'
---

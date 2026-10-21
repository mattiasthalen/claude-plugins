---
type: regex
target: trace
pattern: 'gh pr create(?:(?!gh pr create|\\n\\n)[^\n])*?(?:--base|-B)[\s=]+\\?["'']?csv-export(?![\w-])|gh stack'
---

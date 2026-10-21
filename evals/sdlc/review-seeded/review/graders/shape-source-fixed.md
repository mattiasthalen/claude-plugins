---
type: regex
target: {source: file, path: orders/export.py}
pattern: '\bcsv\.(writer|DictWriter)\b|QUOTE_(MINIMAL|ALL|NONNUMERIC)'
---

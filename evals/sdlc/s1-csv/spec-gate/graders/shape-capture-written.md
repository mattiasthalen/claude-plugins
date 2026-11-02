---
type: regex
target: trace
pattern: 'file_path\\?"?\s*[:=]\s*\\?"?[^"\s\\]*/sdlc(?:-(?!handoff/)[^\s"''\\/]*)?/(?:[^\s"''\\]*/)?capture/ordersdesk/[^\s"''\\]+|"command\\?":\s*\\?"(?=(?:[^"\\]|\\.)*?(?:(?<![0-9&])>(?![&>]?\s*/dev/null)|\btee\s|\bcp\s))(?:[^"\\]|\\.)*?(?<!sdlc-handoff)/capture/ordersdesk/'
---

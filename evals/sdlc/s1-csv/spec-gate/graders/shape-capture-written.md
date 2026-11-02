---
type: regex
target: trace
pattern: 'file_path\\?"?\s*[:=]\s*\\?"?[^"\s\\]*/sdlc(?:-(?!handoff/)[^\s"\''\\/]*)?/(?:[^\s"\''\\]*/)?capture/ordersdesk/[^\s"\''\\]+\\*"\s*,\s*\\*"content\\*"|"command\\?":\s*\\?"(?:[^"\\]|\\.)*?(?<![0-9&<>])>>?\s*(?:\\+"|\'')?[^\s"\''\\&|;<>()]*(?<!sdlc-handoff)/capture/ordersdesk/[^\s"\''\\&|;<>()]+|"command\\?":\s*\\?"(?:[^"\\]|\\.)*?\btee\s+(?:-a\s+)?(?:\\+"|\'')?[^\s"\''\\&|;<>()]*(?<!sdlc-handoff)/capture/ordersdesk/[^\s"\''\\&|;<>()]+|"command\\?":\s*\\?"(?:[^"\\]|\\.)*?(?<![\w-])cp\s+(?:-\S+\s+)*(?!-)(?:[^\s"\\&|;]|\\.)+\s+(?:(?:[^\s"\\&|;]|\\.)+\s+)*?(?:\\+"|\'')?[^\s"\''\\&|;<>()]*(?<!sdlc-handoff)/capture/ordersdesk/'
---

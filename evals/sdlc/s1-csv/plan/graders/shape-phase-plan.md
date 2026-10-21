---
type: regex
target: trace
pattern: 'file_path\\?"?\s*[:=]\s*\\?"?[^"\s\\]*/sdlc(?:-(?!handoff/)[^\s"''\\/]*)?/(?:[^\s"''\\]*/)?phase\\?"[\s\S]{0,60}?content\\?"?\s*[:=]\s*\\?"?plan\b|\b(?:echo|printf)\s+(?:-n\s+)?\\?["'']?plan\b[^\n>]*>\s*\\?["'']?[^\s"''\\]*/sdlc(?:-(?!handoff/)[^\s"''\\/]*)?/(?:[^\s"''\\]*/)?phase\b'
---

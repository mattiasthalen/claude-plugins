---
type: regex
target: trace
pattern: 'file_path\\?"?\s*[:=]\s*\\?"?[^"\s\\]*/sdlc(?:-(?!handoff/)[^\s"''\\/]*)?/(?:[^\s"''\\]*/)?phase\\?"[\s\S]{0,60}?content\\?"?\s*[:=]\s*\\?"?intent\b|\b(?:echo|printf)\s+(?:-n\s+)?\\?["'']?intent\b[^\n>]*>\s*\\?["'']?[^\s"''\\]*/sdlc(?:-(?!handoff/)[^\s"''\\/]*)?/(?:[^\s"''\\]*/)?phase\b|\b(\w+)=\\?["'']?[^\s"''\\]*/sdlc(?:-(?!handoff)[^\s"''\\/]*)?/?\\?["'']?(?=[\s;&])[\s\S]{0,400}?\b(?:echo|printf)\s+(?:-n\s+)?\\?["'']?intent\b[^\n>]*>\s*\\?["'']?\$\{?\1\}?/phase\b'
---

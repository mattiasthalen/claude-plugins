# Vendored

`SKILL.md` and `CREDITS.md` are Matt Pocock's `pr` skill, copied unchanged from [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) at the commit `scripts/vendor.json` pins ([ADR-0013](../../../../docs/decisions/0013-pococks-pr-skill-is-vendored-under-sdlc-with-the-ship-stage-taking-precedence.md)). They change only through `scripts/vendor.sh` (`--refresh` moves the copy, `--check` fails if it has drifted); a repository hook refuses edits by hand. Where they conflict with `sdlc`'s ship stage, the ship stage wins.

They are distributed under the upstream licence:

```
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# Grader samples — capture-build

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### build/graders/shape-capture-copied-before-source.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"# 1. The CSV export follows RFC 4180"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t3","name":"Edit","input":{"replace_all":false,"file_path":"/w/orders/__main__.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t0","name":"Bash","input":{"command":"ls -R sdlc-handoff/capture/ordersdesk"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"C=sdlc-handoff/capture/ordersdesk; mkdir -p docs/decisions && cp \"$C/docs/decisions/0001-the-csv-export-follows-rfc-4180.md\" docs/decisions/"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"# 1. The CSV export follows RFC 4180"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"# 1. The CSV export follows RFC 4180"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t3","name":"Edit","input":{"replace_all":false,"file_path":"/w/orders/__main__.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t0","name":"Bash","input":{"command":"ls -R sdlc-handoff/capture/ordersdesk"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must fail:
```
Next: copy `sdlc-handoff/capture/ordersdesk/` into the repo with `cp -R`, then commit `docs/` with `git commit`.
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/sdlc-handoff/capture/ordersdesk/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"x"}}]},"parent_tool_use_id":null}
```

### build/graders/shape-capture-commit-first.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t4","name":"Bash","input":{"command":"G=/opt/homebrew/bin/git; $G add docs && $G commit -qm \"Record the design: ADR-0001\""}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"# 1. The CSV export follows RFC 4180"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t4","name":"Bash","input":{"command":"git commit -m \"Record the design\" -- docs/"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t3","name":"Edit","input":{"replace_all":false,"file_path":"/w/orders/__main__.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"# 1. The CSV export follows RFC 4180"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t4","name":"Bash","input":{"command":"/opt/homebrew/bin/git add docs/decisions/0001-the-csv-export-follows-rfc-4180.md"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t6","name":"Bash","input":{"command":"python3 -m unittest discover -s tests"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t5","name":"Bash","input":{"command":"/opt/homebrew/bin/git commit -qm \"Record the design\""}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t4","name":"Bash","input":{"command":"git -C \"$R\" add -A && git -C \"$R\" commit -qm \"Record the design\""}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t4","name":"Bash","input":{"command":"G=/opt/homebrew/bin/git; $G add docs && $G commit -qm \"Record the design: ADR-0001\""}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"# 1. The CSV export follows RFC 4180"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t4","name":"Bash","input":{"command":"/opt/homebrew/bin/git add docs/decisions/0001-the-csv-export-follows-rfc-4180.md"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t3","name":"Edit","input":{"replace_all":false,"file_path":"/w/orders/__main__.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t5","name":"Bash","input":{"command":"/opt/homebrew/bin/git commit -qm \"Record the design\""}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t5","name":"Bash","input":{"command":"/opt/homebrew/bin/git commit -qm \"Record the design\""}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must fail:
```
Next: copy `sdlc-handoff/capture/ordersdesk/` into the repo with `cp -R`, then commit `docs/` with `git commit`.
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t6","name":"Bash","input":{"command":"python3 -m unittest discover -s tests"}}]},"parent_tool_use_id":null}
```

### build/graders/shape-only-own-repo-copied.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ordersdesk/. .","description":"Copy the capture into the repo"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t4","name":"Bash","input":{"command":"G=/opt/homebrew/bin/git; $G add docs && $G commit -qm \"Record the design: ADR-0001\""}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t0","name":"Bash","input":{"command":"ls -R sdlc-handoff/capture/ && cat sdlc-handoff/capture/ledger/docs/x.md"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"C=sdlc-handoff/capture/ordersdesk; mkdir -p docs/decisions && cp \"$C/docs/decisions/0001-the-csv-export-follows-rfc-4180.md\" docs/decisions/"}}]},"parent_tool_use_id":null}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/decisions/0001-the-csv-export-follows-rfc-4180.md","content":"# 1. The CSV export follows RFC 4180"}}]},"parent_tool_use_id":null}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/orders/export.py","content":"import csv"}}]},"parent_tool_use_id":null}
```
Must pass:
```
capture/ledger/ belongs to another repo; only capture/ordersdesk/ is copied.
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/. ."}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/ledger/. ."}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/docs/x.md","content":"# Ledger: posting order totals"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"rsync -a \"sdlc-handoff/capture/\" ./"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cat sdlc-handoff/capture/ledger/docs/x.md > docs/x.md"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/ledger/docs/x.md","content":"x"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"cp -R sdlc-handoff/capture/* ."}}]},"parent_tool_use_id":null}
```

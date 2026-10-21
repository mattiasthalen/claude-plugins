# Grader samples — tier-high

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### build/graders/shape-evidence-after-build.md
Must pass:
```
{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/.github/workflows/ci.yml","content":"on: push"}}
{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/T/sdlc-3f2a/evidence.md","content":"# Evidence"}}
```
Must pass:
```
{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/.github/workflows/ci.yml","old_string":"a","new_string":"b"}}
{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/T/sdlc-3f2a/evidence.md","content":"# Evidence"}}
```
Must fail:
```
{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/T/sdlc-3f2a/evidence.md","content":"# Evidence"}}
{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/.github/workflows/ci.yml","old_string":"a","new_string":"b"}}
```
Must fail:
```
{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/.github/workflows/ci.yml","old_string":"a","new_string":"b"}}
{"type":"tool_use","id":"t2","name":"Write","input":{"file_path":"/w/evidence.md","content":"x"}}
```

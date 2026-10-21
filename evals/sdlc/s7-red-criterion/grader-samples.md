# Grader samples — s7-red-criterion

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### build/graders/shape-no-test-edit.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/tests/test_export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":"toolu_01X","session_id":"s"}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/tests/test_export.py","content":"x"}}]},"parent_tool_use_id":"toolu_01X","session_id":"s"}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/orders/export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/tests/test_export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null,"session_id":"s"}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/tests/test_export.py","content":"x"}}]},"parent_tool_use_id":null,"session_id":"s"}
```

### build/graders/shape-no-test-write.md
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/tests/test_export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":"toolu_01X","session_id":"s"}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/tests/test_export.py","content":"x"}}]},"parent_tool_use_id":"toolu_01X","session_id":"s"}
```
Must pass:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/orders/export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Edit","input":{"replace_all":false,"file_path":"/w/tests/test_export.py","old_string":"a","new_string":"b"}}]},"parent_tool_use_id":null,"session_id":"s"}
```
Must fail:
```
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"t1","name":"Write","input":{"file_path":"/w/tests/test_export.py","content":"x"}}]},"parent_tool_use_id":null,"session_id":"s"}
```

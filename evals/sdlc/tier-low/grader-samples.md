# Grader samples — tier-low

Offline samples for every regex shape grader in this scenario. `python3 evals/sdlc/tools/test_shape_graders.py` checks them.

### build/graders/shape-security-pass.md
Must pass:
```
{"type":"tool_use","id":"toolu_1","name":"Skill","input":{"skill":"security-review"}}
```
Must pass:
```
{"type":"tool_use","id":"toolu_2","name":"Agent","input":{"description":"Security lens","prompt":"Review the diff for security issues","subagent_type":"general-purpose"}}
```
Must fail:
```
{"type":"tool_use","id":"toolu_3","name":"Agent","input":{"description":"Docs lens","prompt":"Check the README prose"}}
```
Must fail:
```
{"type":"text","text":"Skipping the security pass."}
```

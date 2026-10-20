---
description: Probe whether the Artifact tool exists in an eval child. Expected to fail (the tool is off in eval runs); if it passes, the publish line in delivering-pitches (ADR-0006) needs an eval that fails without it.
max_turns: 10
allowed_tools: [Artifact, Write, Read]
---

Write a file `probe.html` containing `<title>Probe</title><p>ARTIFACTMARKER-4417</p>`. Then publish it with the Artifact tool. If the Artifact tool does not exist, say exactly that and stop.

# Trigger

Whether `sdlc` fires on its own, without the slash command (A5), and stays out of a conversation that only asks for talk (G1b). Each case grades one Skill call; nothing after it.

**Fixture:** `ordersdesk`.

| Case | Prompt | Graded |
|---|---|---|
| `positive` | "Run the SDLC on this: …" | the Skill tool is called with `sdlc` |
| `negative` | "How would you structure a CSV export … no changes." | no Skill call names `sdlc` |

# Intent

Write the intent as user stories in `intent.md`: each with an id (S1, S2, …), "As a … I want … so that …", acceptance criteria, and notes. An intent with several parts gets a story per part. An intent that already is a story stays one story, refined in place, noting the ticket it came from; offer to update that ticket, and update it only on a yes.

Draft the stories from what the intent says before asking anything: what it leaves open goes into the story's notes as unknown, and the gate asks it.

End at the intent gate. Ask, per story: **now** (deliver it in this run), **file** (file it on the tracker for later; "file" is the yes to file it) or **drop**; when more than one story is now, whether they go as one delivery or one after another; and the seam.

**After the gate**, record each story's disposition and the deliveries in `intent.md` in the run's folder, then:

- **File** each "file" story where the requester says; failing that, where the ticket it came from lives; failing that, where the project's docs (`CLAUDE.md`, memory, config) say; as what they say, with the story's text as the body. The tools in reach never choose the tracker: when none of these names one, ask where, and file nothing until answered. When the requester says there is no tracker, ask what to do with the story. A filing that fails is reported with the story's text, and the run goes on; it tries no other way to file.
- **Every story dropped** ends the run: write `done` to `phase`.
- Otherwise the deliveries run one after another, each from spec.

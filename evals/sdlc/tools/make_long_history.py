"""Make s1-csv/test-long: s1-csv/test with a ~70k-token design interview between /sdlc and the spec gate.

    python3 evals/sdlc/tools/make_long_history.py <repo root>

Spike tooling (per-stage skills spike); not for merge."""
import random, shutil, sys
from pathlib import Path
repo = Path(sys.argv[1]); suite = repo / "evals/sdlc"
src = suite / "s1-csv/test"; dst = suite / "s1-csv/test-long"
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(src, dst, ignore=shutil.ignore_patterns("history.jsonl"))
(dst / "case.yaml").write_text((dst / "case.yaml").read_text().replace("name: s1-test", "name: s1-test-long"))
p = dst / "prompt.md"
p.write_text(p.read_text().replace("S1 test stage, resumed", "S1 test stage after a long interview (~70k tokens of history), resumed"))
fx = suite / "fixtures/ordersdesk"
code = {f: (fx / f).read_text() for f in ["orders/__main__.py", "orders/store.py", "data/orders.json", "tests/test_store.py"]}
rnd = random.Random(7)
customers = ["Lindqvist Bygg AB","Norrlands Café","Åkesson & Dotter","Berg, Hanna","Sjöberg Trading","Ek & Lönn HB","\"Quoted\" Kiosk","Östra Hamnen","Malmö Måleri","Kalix Kaffe; Te"]
def rows(n):
    out = ["id,customer,total,placed_on"]
    for i in range(n):
        c = rnd.choice(customers); c = f"\"{c.replace(chr(34), chr(34)*2)}\"" if any(ch in c for ch in ',"') else c
        out.append(f"{1001+i},{c},{rnd.randint(1,400000)/100:.2f},2026-09-{rnd.randint(1,28):02d}")
    return "\n".join(out)
branches = [
 ("B1","Command shape","where the export lives on the command line",["`orders export --csv PATH`","`orders list --csv PATH`","`orders export PATH --format csv`"]),
 ("B2","Destination","where the CSV goes",["a path argument, required","stdout when no path is given","a path, `-` meaning stdout"]),
 ("B3","Columns","which fields and in what order",["`id,customer,total,placed_on`, the dataclass order","`placed_on,id,customer,total`, date first","a `--columns` option"]),
 ("B4","Quoting","how commas, quotes and newlines in a customer name are written",["`csv.writer` default, QUOTE_MINIMAL","quote every field","escape with backslashes"]),
 ("B5","Encoding","the file's encoding and BOM",["UTF-8, no BOM","UTF-8 with BOM for Excel","a `--encoding` option"]),
 ("B6","Number and date format","how totals and dates are rendered",["`str(Decimal)` and ISO dates","locale formatting","totals in öre as integers"]),
 ("B7","Order of rows","the order rows come out in",["`load_orders()` order (date, then id)","by id","as stored in the JSON"]),
 ("B8","Failures","what an unwritable path or missing flag does",["non-zero exit, OS error on stderr, no traceback","raise and let the traceback show","write to a temp file and rename"]),
]
probes = ["What should happen in the common case?","What about the edge the fixture already holds?","Does this interact with `orders list`?","Is there anything here we must not change?"]
probes = probes + [q + " (second pass, after the answer above)" for q in probes]
turns = []
first_user = "/sdlc Add a CSV export of all orders: `python3 -m orders export --csv <path>` should write every order with a header row."
conv = (src / "conversation.md").read_text()
head, rest = conv.split("## assistant", 1)
assert head.strip().endswith(first_user.strip()) or first_user in head
turns.append(("user", first_user))
files = list(code)
k = 0
for b, title, what, opts in branches:
    for j, probe in enumerate(probes):
        f = files[k % len(files)]; k += 1
        mock = "\n\n".join(f"**Option {chr(65+i)} — {o}**\n\n```text\n$ python3 -m orders export --csv /tmp/out.csv\n$ head -n 12 /tmp/out.csv\n{rows(20)}\n```" for i, o in enumerate(opts))
        a = (f"Design tree so far: {', '.join(x[0] for x in branches[:branches.index((b,title,what,opts))])} closed" if b != "B1" else "Design tree seeded: B1–B8 open.")
        a += f"\n\n**{b} · {title}** ({what}), probe {j+1} of {len(probes)}: {probe}\n\nI read `{f}` again for this one:\n\n```\n{code[f]}\n```\n\n{mock}\n\n"
        a += f"I recommend **Option A** ({opts[0]}): it matches what `orders` already does, keeps `orders list` byte-identical, and is the smallest interface. Which do you want, A, B or C, or something else?"
        turns.append(("assistant", a))
        ans = rnd.choice(["A.", "A, agreed.", "Go with your recommendation.", "A — and keep it boring.", "A. Why not B though? ...ok, A."])
        if k % 9 == 0:
            ans += " Side question: why does store.py sort by (placed_on, id) and not by id?"
        turns.append(("user", ans))
        if k % 9 == 0:
            turns.append(("assistant", "`load_orders` sorts oldest first with id as the tie-break so two orders on one day come out in a stable order; `orders list` prints in that order, which is why B7 option A keeps the export consistent with it. Back to the interview."))
            turns.append(("user", "ok, carry on"))
    turns.append(("assistant", f"**{b} closed:** {opts[0]}. Rationale recorded in the tree. Moving on."))
    turns.append(("user", "next"))
turns.append(("assistant", "All eight branches are closed. Capture is running: `capture/ordersdesk/docs/decisions/0001-csv-export-via-csv-writer.md`, `capture/ordersdesk/docs/lexicon.md`, and the brief in `brief/` beside the spec. Writing the spec now."))
turns.append(("user", "ok"))
md = "\n\n".join(f"## {r}\n{t}" for r, t in turns) + "\n\n## assistant" + rest
(dst / "conversation.md").write_text(md)
print(len(md), "bytes")

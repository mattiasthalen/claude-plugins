## Summary

Adds `python3 -m orders export --csv <path>`: every order in the book, written as UTF-8 CSV (RFC 4180 quoting, no BOM) with the header `id,customer,total,placed_on`, in `list` order. Story S1, delivery d1.

## Testing

| id | criterion | head @ `70147ca` |
|---|---|---|
| C1 | exits 0; header `id,customer,total,placed_on` | ✔ |
| C2 | every order once, in `list` order | ✔ |
| C3 | `Berg, Hanna` stays one field | ✔ |
| C4 | UTF-8, no BOM, `Åkesson & Dotter` intact | ✔ |
| C5 | `89.50`, ISO dates | ✔ |
| E1 | missing `--csv` is a usage error | ✔ |
| P1 | `list` byte-identical | ✔ |
| P2 | data unchanged | ✔ |
| P3 | existing suite passes | ✔ 5/5 |

## Risk

Tier Medium. Two-way door: a new command nothing reads yet. Merge danger: none; one pull request.

## How to revert

`git revert 70147ca 6badc6d`

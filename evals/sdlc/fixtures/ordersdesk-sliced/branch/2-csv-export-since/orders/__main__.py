"""Command line for the order book."""
import argparse
from datetime import date

from orders.export import write_csv
from orders.store import load_orders


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="orders")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="print every order")
    export = commands.add_parser("export", help="write every order to a file")
    export.add_argument("--csv", required=True, metavar="PATH", help="CSV file to write")
    export.add_argument("--since", type=date.fromisoformat, metavar="YYYY-MM-DD",
                        help="only orders placed on or after this date")
    args = parser.parse_args(argv)

    if args.command == "list":
        for order in load_orders():
            print(f"{order.id:>4}  {order.placed_on}  {order.customer:<24} {order.total:>10}")
    elif args.command == "export":
        orders = load_orders()
        if args.since:
            orders = [o for o in orders if o.placed_on >= args.since]
        write_csv(orders, args.csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

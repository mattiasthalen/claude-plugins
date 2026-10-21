"""Command line for the order book."""
import argparse
import sys

from orders.export import write_csv
from orders.store import load_orders


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="orders")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="print every order")
    export = commands.add_parser("export", help="write every order to a file")
    export.add_argument("--csv", required=True, metavar="PATH", help="CSV file to write")
    args = parser.parse_args(argv)

    if args.command == "list":
        for order in load_orders():
            print(f"{order.id:>4}  {order.placed_on}  {order.customer:<24} {order.total:>10}")
    elif args.command == "export":
        try:
            write_csv(load_orders(), args.csv)
        except OSError as e:
            print(f"orders: {e}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

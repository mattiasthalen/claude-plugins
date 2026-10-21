"""Command line for the order book."""
import argparse

from orders.store import load_orders


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="orders")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="print every order")
    args = parser.parse_args(argv)

    if args.command == "list":
        for order in load_orders():
            print(f"{order.id:>4}  {order.placed_on}  {order.customer:<24} {order.total:>10}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

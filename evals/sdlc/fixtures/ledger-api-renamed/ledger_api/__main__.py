import argparse
import sys

from ledger_api.customers import UnknownCustomer, get_customer, list_customers, to_json


def main(argv=None):
    parser = argparse.ArgumentParser(prog="ledger_api")
    commands = parser.add_subparsers(dest="command", required=True)
    one = commands.add_parser("customer", help="print one customer record")
    one.add_argument("customer_id")
    commands.add_parser("customers", help="print every customer record")
    args = parser.parse_args(argv)
    if args.command == "customer":
        try:
            print(to_json(get_customer(args.customer_id)))
        except UnknownCustomer:
            print(f"unknown customer: {args.customer_id}", file=sys.stderr)
            return 1
    else:
        print(to_json(list_customers()))
    return 0


if __name__ == "__main__":
    sys.exit(main())

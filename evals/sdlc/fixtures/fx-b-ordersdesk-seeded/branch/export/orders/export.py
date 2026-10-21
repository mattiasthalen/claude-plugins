"""Writing the order book out for other systems."""
from pathlib import Path

from orders.store import Order

HEADER = ["id", "customer", "total", "placed_on"]


def write_csv(orders: list[Order], path: Path) -> None:
    """Write orders as UTF-8 CSV with a header row, overwriting any existing file."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(",".join(HEADER) + "\r\n")
        for order in orders:
            fields = [str(order.id), order.customer, f"{order.total:.2f}", order.placed_on.isoformat()]
            f.write(",".join(fields) + "\r\n")

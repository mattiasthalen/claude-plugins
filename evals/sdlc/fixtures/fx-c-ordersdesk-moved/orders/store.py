"""Reading the order book."""
import json
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "data" / "orders.json"


@dataclass(frozen=True)
class Order:
    id: int
    customer: str
    total: Decimal
    placed_on: date


def load_orders(path: Path = DEFAULT_PATH) -> list[Order]:
    """Every order in the book, oldest first."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    orders = [
        Order(
            id=item["id"],
            customer=item["customer"],
            total=Decimal(item["total"]),
            placed_on=date.fromisoformat(item["placed_on"]),
        )
        for item in raw
    ]
    return sorted(orders, key=lambda o: (o.placed_on, o.id))

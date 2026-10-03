"""Tiny price-time-priority teaching simulator.

This is deliberately single-threaded and in-memory. It is not a production
matching engine: it omits validation, integer tick/lot units, persistence,
risk checks, self-trade prevention, special time-in-force rules, and market
orders.
"""

from dataclasses import dataclass
from itertools import count

_sequence = count()


@dataclass
class Order:
    order_id: str
    side: str
    price: int
    qty: int
    sequence: int


class Book:
    def __init__(self):
        self.bids = []
        self.asks = []
        self.trades = []

    def add_limit(self, order_id, side, price, qty):
        if side not in {"BUY", "SELL"} or qty <= 0 or price <= 0:
            raise ValueError("side must be BUY/SELL and price/qty must be positive")

        incoming = Order(order_id, side, price, qty, next(_sequence))
        opposite = self.asks if side == "BUY" else self.bids
        resting_side = self.bids if side == "BUY" else self.asks

        while incoming.qty and opposite:
            resting = opposite[0]
            crosses = price >= resting.price if side == "BUY" else price <= resting.price
            if not crosses:
                break

            fill_qty = min(incoming.qty, resting.qty)
            self.trades.append((incoming.order_id, resting.order_id, resting.price, fill_qty))
            incoming.qty -= fill_qty
            resting.qty -= fill_qty
            if resting.qty == 0:
                opposite.pop(0)

        if incoming.qty:
            resting_side.append(incoming)
            if side == "BUY":
                resting_side.sort(key=lambda o: (-o.price, o.sequence))
            else:
                resting_side.sort(key=lambda o: (o.price, o.sequence))

        return incoming.qty

    def show(self):
        print("Trades (taker, maker, price, qty):")
        for trade in self.trades:
            print(" ", trade)
        print("Bids:", [(o.price, o.qty, o.order_id) for o in self.bids])
        print("Asks:", [(o.price, o.qty, o.order_id) for o in self.asks])


if __name__ == "__main__":
    book = Book()
    book.add_limit("Alice", "SELL", 100, 2)
    book.add_limit("Bo", "SELL", 101, 1)
    book.add_limit("Chen", "SELL", 100, 3)
    remaining = book.add_limit("Dana", "BUY", 100, 4)
    book.show()
    print("Dana remaining:", remaining)

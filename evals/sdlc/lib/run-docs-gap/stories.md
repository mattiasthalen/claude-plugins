# Intent: orders count

Source: the requester, in this session.

## Why
The back office answers "how many orders do we have?" several times a day by counting `orders list` lines by hand.

## Non-goals
- Changing what `orders list` prints.

## S1. Count the orders
As a back-office clerk, I want `orders count` to print how many orders there are, so that I stop counting list lines.

Disposition: now

Acceptance criteria:
- [stated] Given the order book, when I run `orders count`, then it prints the number of orders and nothing else.
- [stated] Given orders placed on several days, when I run `orders count --since 2026-09-03`, then it prints how many were placed on or after that day.
- [proposed] Given an empty order book, when I run `orders count`, then it prints 0 (why I proposed it: an empty book is the first edge a clerk meets).

## S2. Count by customer
As a back-office clerk, I want a count per customer, so that I can see who orders most.

Disposition: later

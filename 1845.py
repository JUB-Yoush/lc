"""
bf: simply rescan the list whenever a new seat is added/removed.
How to maintain which seat is the minimum unreserved
sets have fast lookup but are unsorte
arrays are sorted but have slow lookup?
    yeah, we'd have to check at worst n places to find it
stack: we arrange things in decreasing order, top of stack is lowest, but re-inserting would take n space (move everything around it)
actually we'd never replace (yes we would
if 12345
2345
345
45
245
3245
^ it's over
queue: we always want to place the higest, so queue wouldn't work (bigger would be above lower)
keep a pointer on the smallest non-reserved spot?
we'd have to re-calculate it
heap.
inserting and removing are logn
make list of 1 - n
heapify
pop and push
profit.
"""

import heapq


class SeatManager:
    def __init__(self, n):
        self.seats = list(range(1, n + 1))
        heapq.heapify(self.seats)

    def reserve(self):
        seat = heapq.heappop(self.seats)
        return seat

    def unreserve(self, seatNumber):
        heapq.heappush(self.seats, seatNumber)

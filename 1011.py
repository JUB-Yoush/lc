"""
pick the capacity so that you can transfer everything in time
binary search
what is the lowest value we could pick
1
highest?
weights/ships I think
no because the numbers aren't evenly distributed
weights/ships OR largest value
I think
must be shipped in given order
hmmmmmm
pick a size
see how many ships it takes
if less, decrease weight
if more, increase weight
if equal, decrease weight by 1 until it drops below to ensure we have the minimum value?
min 1
max sum
"""

from re import search


class Solution:
    def shipWithinDays(self, weights: list[int], ships: int) -> int:
        def simsearch(mid) -> int:
            # gets the number of trips required
            i = 0
            remaining = mid
            ships = 0
            while i < len(weights):
                if remaining - weights[i] > -1:
                    remaining -= weights[i]
                    i += 1
                else:
                    remaining = mid
                    ships += 1

            return ships

        def can_ship(mid):
            curr_ships, curr_capacity = 1, mid
            for w in weights:
                if curr_capacity - w < 0:
                    curr_ships += 1
                    if curr_ships > ships:
                        return False
                    curr_capacity = mid
                curr_capacity -= w
            return True

        lo = max(weights)
        hi = sum(weights)
        res = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_ship(mid) <= ships:
                res = min(res, mid)
            else:
                lo = mid + 1
        return res

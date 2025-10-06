"""
you can pick number or skip number
once k numbers, append result to list
use list.copy because pointer reference stuff
"""


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def pick(picks: list[int], curr):
            if len(picks) == k:
                res.append(picks.copy())
                return

            if curr > n or len(picks) > k:
                return

            picks.append(curr)
            pick(picks, curr + 1)
            picks.remove(curr)
            pick(picks, curr + 1)

        pick([], 1)
        return res

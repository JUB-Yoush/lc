"""
easier coin change?
coin change but greedy works?
if 5 -> no change
if 10 -> 5
if 20 -> 10 + 5
manage count in a map?
is there something I'm missing?
"""


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] < 1:
                    return False
                change[5] -= 1
                change[10] += 1
            elif bill == 20:
                if change[10] > 1 and change[5] > 1:
                    change[5] -= 1
                    change[10] -= 1
                    change[20] += 1
                elif change[5] >= 3 and change[10] < 1:
                    change[5] -= 3
                    change[20] += 1
                else:
                    return False

        return True


print(Solution.lemonadeChange(None, [5, 5, 5, 10, 20]))

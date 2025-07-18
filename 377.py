"""
backtracking?
we need to return number, not the specific combos
might not be backtracking then
dp? how
wait this is coin change
coin changeish
bf: backtracking generation
how to make smarter
we can check if we can make coin + remainder
1 + all the ways we can generate 3
1 + 1 + all the ways we can generate 2
"""


class SolutionCoin:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # holds how many ways we can generate a given number
        cache = [0] * target

        # we can always make a value if we have that coin
        for n in nums:
            cache[n] = 1

        # given value, return number of ways to get that value
        def getWays(subtarget):
            if subtarget == 0:
                return 0
            for n in nums:
                if n <= subtarget:
                    return 1 + getWays(subtarget - n)
            pass


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {0: 1}

        def pick(sum):
            if sum in memo:
                return memo[sum]

            res = 0
            for n in nums:
                if sum < n:
                    break
                res += pick(sum - n)
            memo[sum] = res
            return res

        pick(0)
        return memo[target]

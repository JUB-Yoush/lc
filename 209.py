"""
huh
so it's a window of the array
min length, we don't have to show our work
if we want it to be o(n) then we can't sort it
we can't sort it anyway because the order needs to be maintained

"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]  # extend window up
            while (
                total >= target
            ):  # slide window back in when we're over target (looking for lowest)
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res


print(Solution.minSubArrayLen(None, 11, [1, 2, 3, 4, 5]))

"""
how do we know when to stop looking?
when left has reached the original left?
use k algo for cases in the middle
for cases that wrap, just wrap the numbers around and don't add the same value twice
"""


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        curr_max = 0
        global_max = nums[0]
        curr_min = 0
        global_min = nums[0]
        total = sum(nums)
        for n in nums:
            curr_min = min(curr_min + n, n)
            curr_max = max(curr_max + n, curr_max)
            global_max = max(curr_max, global_max)
            global_min = min(curr_min, global_min)

        if global_max < 0:
            return global_max
        return max(global_max, total - global_min)

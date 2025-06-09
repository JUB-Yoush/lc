"""
max I could get from robbing this house OR the max I could get from skipping this house (start from house to the right)
cache only needs to be 2 long (only care about max from last 2 houses)
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        cache = [0, 0]
        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            tmp = cache[1]
            cache[1] = max(cache[0] + nums[i], cache[1])  # rob house or skip house
            cache[0] = tmp

        return cache[1]

# https://leetcode.com/problems/contains-duplicate-ii/description/
"""
use a fixed sliding window and a set
when value exists in set return
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l = 0
        r = 0
        window = set()

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])

        return False

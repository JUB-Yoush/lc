"""
bin search
if not there return middle of r and l I guess?
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if nums[r] < target:
            return 0
        if nums[l] > target:
            return len(nums)

        while l < r:
            m = (l + r) // 2
            if r - l == 1:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                return l + 1
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            if nums[m] < target:
                l = m

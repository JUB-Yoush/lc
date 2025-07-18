"""
it's a sorted array but we aren't told where it was rotated from
we need to compare numbers
when i > i+1 then that value is out of order
it could've just been sorted n times and look the same, cut might not exist
would be easy except logn requirement
we need to do a binary search... if we have high mid and low:
    if high < mid then cut between high and mid
    if low > mid then cut between low and mid
    only one of these cases can exist
    when m out of order with L or R and they're next to each other, we've found the out of order value.
"""


class Solution:
    def findMin(self, nums) -> int:
        hi = len(nums) - 1
        lo = 0
        if nums[lo] < nums[hi] or len(nums) == 1:
            return nums[lo]

        while True:
            mid = (hi + lo) // 2
            if nums[hi] < nums[mid]:
                if hi - mid <= 1:
                    return min(nums[mid], nums[hi])
                else:
                    lo = mid

            if nums[lo] > nums[mid]:
                if mid - lo <= 1:
                    return min(nums[mid], nums[lo])
                else:
                    hi = mid


print(Solution.findMin(None, [3, 4, 5, 0, 1, 2]))


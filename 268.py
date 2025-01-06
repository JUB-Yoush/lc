"""
constant space
linear runtime
how
bf:
- loop over the array n times, check for 0-n
- hashing
values are unsorted
but we know it's range
bucketsort?
no, constant memory
not a lot of data structures to use
"""

"""
requires math trick... it's mid
bitwise XOR or use the 
sum of range - sum of input = missing value
"""


class Solution:
    def missingNumber(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

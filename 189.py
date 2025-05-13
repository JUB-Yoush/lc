"""
constant extra space
no list library stuff either ig
store nth value
shift everything up, put null in 0
replace 0 wtih nth value
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop())
        pass

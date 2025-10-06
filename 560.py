"""
two pointers?
no, negative numbers
are the lists sorted?
no
cant sort list either
prefix sums

use a map of prefix sum -> count
look for sum - k, as that is

steps:
    calculate prefix
    check if prefix -k exists in the map

"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_freq = {}
        prefix_freq[0] = 1
        res = 0
        sum = 0
        for n in nums:
            sum += n
            if sum - k in prefix_freq:
                res += prefix_freq[sum - k]

            if sum not in prefix_freq:
                prefix_freq[sum] = 0
            prefix_freq[sum] += 1

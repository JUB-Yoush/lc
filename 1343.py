"""
all subarrays are the same size
just slide the window, check, and increment
"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        if len(arr) <= 2:
            return 0
        l = 0
        r = 0
        curr = 0
        res = 0
        while r < len(arr):
            if r - l >= k:
                curr -= arr[l]
                l += 1
                curr += arr[r]

            else:
                curr += arr[r]
            if (curr / k) >= threshold and r + 1 - l >= k:
                res += 1
            r += 1
        return res


print(Solution.numOfSubarrays(None, [1, 1, 1, 1, 1], 1, 0))

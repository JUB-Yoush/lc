"""
get all sequence starts
loop over those, check for longest sequence
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        highest = 0
        hashnums = set(nums)
        # starts = []
        for n in nums:
            if (n - 1) not in hashnums:
                record = 1
                curr = n
                while curr + 1 in hashnums:
                    record += 1
                    curr += 1
                highest = max(record, highest)
                # starts.append(n)

        # for s in starts:
        #     record = 1
        #     curr = s
        #     while curr + 1 in hashnums:
        #         record += 1
        #         curr += 1
        #     highest = max(record, highest)
        return highest

#!/usr/bin/env python3
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        at ever step we can either chose to add a number or add no number
        """
        output = 0
        i = 0

        def pick(curr):
            nonlocal output
            # finished picking
            if i == len(nums):
                output.append(curr_set.copy())
                return
            # pick one, recurse, don't pick one, don't recurse
            curr_set.append(nums[i])
            choice(curr_set,i+1)
            curr_set.pop()
            choice(curr_set,i+1)
        # driver
        chose([],0)
        return output

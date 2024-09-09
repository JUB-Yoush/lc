#!/usr/bin/env python3
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        pick a number, recurse wtih that arr and target - work
        """
        output = []

        def pick(i,choices, target_remaining):
            nonlocal output
            if target_remaining < 0:
                return
            if target_remaining == 0:
                output.append(choices.copy())
                return
            pick(i,choices,target_remaining)
            new_target -= canidates[i]
            choices.append(canidates[i])
            pick(i+1,choices,new_target)

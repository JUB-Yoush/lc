#https://leetcode.com/problems/concatenation-of-array/description/
'''
you're combining two arrays together
just make an array of twice the size, loop through and reallocate?
'''


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = nums + nums
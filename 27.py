#https://leetcode.com/problems/remove-element/description/
'''
we can use what we learned from 26
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums):
            while  j < len(nums) and nums[j] == val:
                j += 1
            if j == len(nums):
                break
            nums[i],nums[j] = nums[j], nums[i]
            while nums[i] != val:
                i+=1
        return i -1

print(Solution.removeElement(None,[0,1,2,2,3,0,4,2],2))




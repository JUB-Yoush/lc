#https://leetcode.com/problems/remove-element/description/
'''
move bad number all the way to the end
but moving every bad number all the way to the end would be a n^2 solution
'''
# soln
'''
use index to keep track of next avalable spot
re-assign every value while ignoring the target ones
'''
class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		index = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[index] = nums[i]
				index+=1
		return index



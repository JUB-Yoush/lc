import copy

#https://leetcode.com/problems/subsets-ii/
'''
elements can be not unique
how do we account for this
start with []
add i or []
move to next number
the only change would be in checking for duplicates?
but not rlly cuz we treat each number as it's index and not it's value
I'll see when I start coding
no we'd get duplicates
in [1,2,2] we'd have two [2] subsets
that's the rub
'''
#neetcodeish soln
class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		res = []
		nums.sort()
		def recurse(i,num_set):
			if i== len(nums):
				res.append(num_set[::])
				return
			#subsets that include nums[i]
			num_set.append(nums[i])
			recurse(i+1,num_set)
			num_set.pop() # undo append


			# don't include nums[i] or any of it's copies if it appears twice
			while i + 1 < len(nums) and nums[i] == nums[i+1]:
				i += 1
			recurse(i+1,num_set)

		recurse(0,[])
		return res
			

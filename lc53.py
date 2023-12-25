#https://leetcode.com/problems/maximum-subarray/description/
'''
loop through numbers and add values
if sum is negative, reset to 0 (equivalent of ignoring all previous numbers)
maintain and return highest sum
'''
class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_sum = nums[0]
		curr_sum = 0
		for num in nums:
			curr_sum = max(curr_sum,0) # reset to 0 if negative
			curr_sum += num
			max_sum = max(max_sum,curr_sum)
		return max_sum

#https://leetcode.com/problems/maximum-sum-circular-subarray/description/
'''
the array can wrap around
how does this change the problem
numbers on the edges can talk to each other
when do we stop?
when we've wrapped around?
yeah when DO we stop?
start at index 0
'''
#neetcode soln
class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		n = len(nums)
		globalMax, globalMin = nums[0],nums[0]
		curMax, curMin = 0,0
		total = 0
		for n in nums:
			curMax = max(curMax + n,n)
			curMin = min(curMin+n,n)
			total += n
			globalMax = max(globalMax,curMax)
			globalMin = max(globalMin,curMin)
		
		return max(globalMax,total - globalMin) if globalMax > 0 else globalMax

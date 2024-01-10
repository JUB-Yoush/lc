#https://leetcode.com/problems/house-robber-ii/
'''
how does the culdesac change things?

'''
class Solution:
	def rob(self, nums: List[int]) -> int:
		def helper(nums):
			dp = [0] * 2
			for n in nums:
				new_total = max(n+ dp[0],dp[1])
				dp[0] = dp[1]
				dp[1] = new_total
			return max(dp[0],dp[1])
		return max(nums[0], helper(nums[:-1]),helper(nums[1:]))
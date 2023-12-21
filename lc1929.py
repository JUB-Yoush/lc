class Solution:
	def getConcatenation(self, nums: List[int]) -> List[int]:
		ans = [0] * (len(nums)*2) 
		index = 0
		for num in nums:
			ans[index] = num
			ans[index + len(nums)] = num
			index += 1
		return ans

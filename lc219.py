#https://leetcode.com/problems/contains-duplicate-ii/description/
'''
use a fixed sliding window and a set
when value exists in set return
'''
class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		l = 0
		r = 0 
		window = set()

		while r < len(nums):

			if r - l + 1 > k:
				window.remove(nums[l])
				l+= 1

			if nums[r] in window:
				return True
			window.add(nums[r])

		return False
			
import heapq

#https://leetcode.com/problems/kth-largest-element-in-an-array/
'''
convert to heap (make numbers negative)
pop k-1 elems
return kth * -1
'''
class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		nums = [-x for x in nums]
		heapq.heapify(nums)
		for i in range(k-1):
			heapq.heappop(nums)
		return heapq.heappop(nums) * -1





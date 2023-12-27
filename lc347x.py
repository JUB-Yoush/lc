#https://leetcode.com/problems/top-k-frequent-elements/
import heapq
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		res = []
		frequency = {}
		#populate hashmap
		for num in nums:
			if num not in frequency:
				frequency[num] = 0
			frequency[num] += 1

		values = frequency.values()
		
       
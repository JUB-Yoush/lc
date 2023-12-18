#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
two pointers
one on left one on right
or start next to each other
how to know when to move right one and when to move the left one
if on opposite sides, moving left increases sum while right decreases sum
if next to each other then they both increase
so on 0 and len-1
if value is too high, move right down
if value too low, move left up
'''
class Solution:
	def twoSum(self, numbers: list[int], target: int) -> list[int]:
		l = 0
		r = len(numbers) -1
		while True: # answer exists so we'll break eventually
			sum = numbers[l] + numbers[r]
			if sum == target:
				break
			if sum > target:
				r -= 1
			if sum < target:
				l += 1
		return [l+1,r+1] # 1 indexed apparently
      


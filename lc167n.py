class Solution:
	def twoSum(self, numbers: list[int], target: int) -> list[int]:
		l = 0
		r = len(numbers) -1
		while l < len(numbers):
			if numbers[l] + numbers[r] == target:
				return [l+1,r+1]
			if numbers[l] + numbers[r] > target:
				r-=1
			if numbers[l] + numbers[r] < target:
				l+=1
			
				
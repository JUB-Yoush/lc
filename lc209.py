#https://leetcode.com/problems/minimum-size-subarray-sum/
'''
sliding window
l and r are bounds, get bigger or smaller
return smallest subarray of sum
when do we move right out?
bf:
- check every subarray
- keep track of size of those equal or greater than target
- return lowest
start l,r at 0
it's not sorted so doesn't have to be at other end
move r up, add to sum
if sum >= t then update the lowest subarr (get the distance from l and r)
if lower, then move l up?
moving l up just lets us use another number
current issues:
	- how do l and r move so that every subarray is considered?
	- instead think of when to grow window and when to shrink window?
	- when to add new values to the window
	- if >= target, then sliding window up OR moving l in would change the set
	- but the goal is to have the smallest set possible
	- so maybe when >= target move L in until no longer greater than target, then move R up?
[231243]7
[lxxxxx]
[rxxxxx]
sum = 0
msa = 6
'''
class Solution:
	def minSubArrayLen(target, nums):
		l = 0
		r = 0
		sum = 0
		min_subarr = len(nums) + 1
		if len(nums) == 0:
			return nums[0]
		while r != len(nums)+1 or l>r:
			if sum >= target:
				min_subarr = min(min_subarr,(r-l))
				sum -= nums[l]
				l += 1
				continue
			if r < len(nums):sum += nums[r]
			r+= 1
		if min_subarr == len(nums) + 1: return 0
		return min_subarr

print(Solution.minSubArrayLen(7,[2,3,1,2,4,3]))	


			

			



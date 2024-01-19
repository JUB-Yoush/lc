#https://leetcode.com/problems/jump-game-ii/
'''
we need to keep track of the number of jumps it takes to reach any specific point
[2,3,1,1,4]
[0,1,1,2,2]
return the value at the last index

how did I get those numbers?
0: starting index
1: 2nd index, 2 has a jump power of 2, we can reach 1st from 0th
1: 0th index has 2
2: 0(2) + 2(1), or 0(2) + 1(3)
2: 0(2) + 1(3)
consider the jump power as well as the distance from the current index
but checking every prior jump combo would be slow
take current jumps count
take your jump power
for all the values you could reach with your current jump power and that DONT have a jump power above 0, assign them your jump count +1
'''
class Solution:
	def jump(self, nums):
		jumps_required = [0] * len(nums)
		#jumps_required[0] = -1
		# current value can never be zero
		for i in range(len(nums)):
			# loop over every value it could reach
			for j in range(1,nums[i]+1):
				if i+j < len(nums) and jumps_required[i+j] <1:
					jumps_required[i+j] = jumps_required[i] + 1
		return jumps_required[-1]


print(Solution.jump(None,[2,3,1,1,4]))
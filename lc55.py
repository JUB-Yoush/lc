#https://leetcode.com/problems/jump-game/description/
'''
the jump len represnets the # of indexes I can go up
if the jump len is higher then the remaining indexes automatically return true
for all the indexes I can go to, pick the highest one
it would be jump len - position in array in reverse
[2,3,1,1,4]
at 2, jump len would let us go to [3,1]
3 - 1 because it's one away from the front
1 - 0 because it's 0 away from the front
distance of 3 = 3 - 1 = 2
distance of 1 = 1 - 0 = 1
we always pick the highest value
repeat until base case
if the largest distance is a 0 then return false
'''
class Solution1:
	def canJump(self, nums) -> bool:
		i = 0
		while True:
			#base case (can jump past the end)
			if i + 1 + nums[i] >= len(nums):
				return True
			# group of potential values we could jump to
			#jump_range = nums[i+1:nums[i]+1]
			jump_range = []
			jump = nums[i]
			i+= 1
			for j in range(jump):
				jump_range.append(nums[i+j])
				
			max_distance = 0
			max_distance_index = i
			for j in range(len(jump_range)):
				distance = jump_range[j] - (len(jump_range) - j -1)
				if distance >= max_distance:
					max_distance = distance
					max_distance_index = i + j
			i = max_distance_index
			if nums[i] == 0:
				return False

#dp!?
# check if last-1 can reach last
# if so decrement last
# if last == 0 then return true
'''
[2,3,1,1,4]

[3,2,2,0,4]
'''
class Solution:
	def canJump(self, nums) -> bool:
		goal = len(nums) -1
		i = len(nums) -2
		while i >= 0:
			if nums[i] >= (goal-i):
				goal -= 1
			i-=1
		return goal == 0


print(Solution.canJump(None,[2,3,1,1,4]))




class Solution2:
	def canJump(self, nums) -> bool:
		
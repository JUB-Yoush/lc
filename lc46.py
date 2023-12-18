#https://leetcode.com/problems/permutations/
'''
pick number not in list (treat like a set somehow)
once set = len
append to res
how to pick the numbers?
rng? no. would be very slow
branch, at each step you can:
- add any other value
use a for loop
for value in remaining:
	add(value,remaining.pop(value))
'''
class Solution:
	def permute(self, nums):
		res = []
		#values we've added and the remaining ones to pick from
		def add(curr_list,remaining):
			nonlocal res
			nonlocal nums
			# base case
			if len(curr_list) == len(nums):
				res.append(curr_list.copy())
				return

			for i,value in enumerate(remaining):
				# add a value and remove from pool
				curr_list.append(value)
				remaining.pop(0)
				add(curr_list.copy(),remaining.copy())
				#okay undo that
				used = curr_list.pop()
				remaining.append(used)

	
		add([],nums.copy())
		return res

sol = Solution()
print(sol.permute([1,2,3]))


#neetcode sol
#The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

class Solution:
	def permute(self, nums):
		result = []
		if len(nums) ==1:
			return [nums.copy()]
		perms = self.permute(nums)
		for i in range(len(nums)):
			n = nums.pop(0)

			for perm in perms:
				perm.append(n)
			result.extend(perms)
			nums.append(n)
		return result
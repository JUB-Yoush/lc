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
class Solutionold:
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



#neetcode sol
#The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

class Solutionneet:
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

# new sol
class Solution:
	def permute(self, nums):
		output = []
		def helper(curr,remaining):
			if len(curr) == len(nums):
				output.append(curr.copy())
				return
			looper = remaining.copy()
			for num in looper:
				curr.append(num)
				remaining.remove(num)
				helper(curr,remaining)
				curr.remove(num)
				remaining.append(num)
		helper([],nums.copy())
		return output

print(Solution.permute(None,[1,2,3]))
#https://leetcode.com/problems/subsets/
"""
return powerset of array 
all # are unique
make an empty subset
add one value (value to the left) to it and check if exists in set
order does not matter (sets not arrays)
if new array then append to set
if not new then pick a different number
stop when subsets.len = 2^n?
should be recursive though
when does it end: when subset.len = 2^n
"""

class Solution:
	def subsets(self, nums):
		subsets = set()
		def add_value(subset,index):
			subsets.add(subset)
			#if still within array, add value or skip value
			if index != len(nums):
				add_value(subset,nums[index +1])
				subset.append(nums[index])
				add_value(subset,nums[index +1])
		
		add_value([],0)
		return subsets

# neetcode soulution (mine don't work cuz mutability stuff w python)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

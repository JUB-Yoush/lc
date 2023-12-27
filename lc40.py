#https://leetcode.com/problems/combination-sum-ii/description/
'''
sorting in these problems is fine considering the massive time complexities they usually have
if we sort the list then I can move through the array in some sensible order
at every point I can either 
- add nothing
- add value
then move to next value in array
if sum + number is larger then target then nothing else will be smaller, it's a dead route
you can think of it like a maze sorta?
how do I prevent duplicate (looking) routes from showing up?
'''
# returns dupes sorta
class Solution:
	def combinationSum2(candidates, target):
		candidates.sort()
		res = []
		def dfs(curr_list,i):
			nonlocal candidates
			if sum(curr_list) == target:
				res.append(curr_list.copy())
				return
			elif sum(curr_list) > target:
				return
			if i == len(candidates):
				return
			curr_list.append(candidates[i])
			dfs(curr_list,i+1)
			skipped_val = curr_list.pop()
			while candidates[i] == skipped_val:
				i+=1
				if i == len(candidates):
					return
			dfs(curr_list,i)
		dfs([],0)
		return res

print(Solution.combinationSum2([10,1,2,7,6,1,5],8))
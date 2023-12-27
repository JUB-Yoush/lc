#https://leetcode.com/problems/combination-sum/
"""
<<<<<<< HEAD
what is the thinking process for adding numbers?
because the system otherwise is fairly simple:
- pick a number + add to current sum
- if current sum == target: check if combination already exists in hash
- if dont exist then add
- continute until every option exausted
- so start with an empty list
- make the decision to add [] or that number
- but you can add numbers repeatedly so when do you... stop adding that number
- [], current number, or move to next number
- three branches instead of two?
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass
=======
start with []
at every step:
- add current #
- add next #
- add nothing
- if at target, check list in hash then return
- if > target then break 
"""
# neetcode sol but I wanted to look at it and know how to write the solutions for these
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy()) # create deep copy so it doesn't continue to be modified
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop() # take the change OFF the menu
            dfs(i+1,cur,total)
        
        dfs(0,[],0)
        return res
>>>>>>> a54848d42bb7c3a717a73b18140bd7ef8e188ed9

#https://leetcode.com/problems/combination-sum/
"""
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

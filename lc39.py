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
class Solutionq:
    def combinationSum(self, candidates, target: int):
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

'''
 we can pick the current number, or move to next number
 if the sum is at target, append
 if the sum is over target, don't append
'''
class Solution:
    def combinationSum(self, candidates, target: int):
        combos = []

        def choice(choices,i):
            if sum(choices) == target:
                combos.append(choices.copy())
            elif sum(choices) > target:
                # pick current number again, or move to next number
                if i < len(candidates):
                    choices.append(candidates[i])
                    choice(choices,i)
                    choices.pop()
                    choice(choices,i+1)
        choice([],0)
        return combos
                
print(Solution.combinationSum(None,[2,3,6,7],7))



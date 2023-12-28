#https://leetcode.com/problems/generate-parentheses/
'''
backtracking problem
for every bracket I could:
- close it
- make another open one
- the amount of open ones I have need to match the amount of closed ones
if we only have to make one:
no open brackets: make a bracket
(
at open bracket limit, have to close it
use a stack to manage which brackets are open or closed
whenever we make a new open bracket we need to increase the number of pairs we're going to make
once it's at capacity we can only make closing brackets
'''
class Solution:
    def generateParenthesis(self, n: int):
        sets = []
        def backtrack(current_brackets,opens,closeds):
            # at every step we can add another or close
            if opens == n:
                if closeds != n:
                    backtrack(current_brackets+")",opens,closeds+1)
                else:
                    sets.append(current_brackets)
            else:
                backtrack(current_brackets+"(",opens+1,closeds)
                if closeds < opens:
                    backtrack(current_brackets+")",opens,closeds+1)
        backtrack("",0,0)
        return sets

print(Solution.generateParenthesis(None,2))
                
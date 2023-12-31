'''
add values to stack 
make a mapping of opening and closing brackets
add openeings to stack 
if closing then check if opening is at top of stack 
if not then bad
'''
class Solution:
    def isValid(self, s: str) -> bool:
        ref = {'(':')','{':'}','[':']'}
        stack = []
        #if len(s) == 1:return False
        for c in s:
            if c in ref:
                stack.append(c)
            elif len(stack) > 0 and c == ref[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) ==0

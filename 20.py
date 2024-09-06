#https://leetcode.com/problems/valid-parentheses/
'''
- check left and right brackets in key value pairs
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ref = { "]":"[",")":"(","}":"{"}
        stack = []
        for i in range(0,len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) > 0 and stack[-1] == ref[s[i]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

print(Solution.isValid(None,"()[]{}"))
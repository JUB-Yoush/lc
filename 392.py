#https://leetcode.com/problems/is-subsequence/description/
"""
just use a pointer?
and make sure they're in order?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        while ptr < len(s):
            if s[ptr] == t:
                ptr += 1
            t+= 1
            if t == len(t):
                return False
        return True
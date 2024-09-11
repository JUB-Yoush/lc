#https://leetcode.com/problems/is-subsequence/description/
"""
just use a pointer?
and make sure they're in order?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        i = 0
        while ptr != len(s):
            if i == len(t):
                return False
            if s[ptr] == t[i]:
                ptr += 1
            i += 1
        return True


print(Solution.isSubsequence(None,"abc","ahbgdc"))
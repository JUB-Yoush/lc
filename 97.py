"""
add a and b together
form a set
form set of c
check if s1 == s2
nvm I had it wrong

check current c value
check if a or b could supply that value
if ya, pop and check for rest of a and b
make sure you don't use all of a or b before using another
"""

from collections import Counter


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a_len = len(s1)
        b_len = len(s2)
        # must be same len
        if len(s1 + s2) != len(s3):
            return False

        def iter(a, b, c):
            # we've used all of one but none of the other (not interleaved)
            if (len(a) == 0 and len(b) == b_len) or (len(b) == 0 and len(a) == a_len):
                return False

            if len(a) == 0 and len(b) == 0 and len(c) == 0:
                return True

            if len(a) > 0 and a[0] == c[0]:
                a.pop(0)
                c.pop(0)
                return iter(a.copy(), b.copy(), c.copy())
            if len(b) > 0 and b[0] == c[0]:
                b.pop(0)
                c.pop(0)
                return iter(a.copy(), b.copy(), c.copy())

        return iter(list(s1), list(s2), list(s3))


print(Solution.isInterleave(None, "aabcc", "dbbca", "aadbbcbcac"))

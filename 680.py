"""
just treat like normal palindrome question, (work inward from outside)
if paleindrome breaks, just try skipping a letter on the left or the right n see if fixed
if STILL broken... it's over.
"""

"""
Solution:
you can check a palindrome by inverting the string.
if you
"""


# neet
class Solution:
    def validPalindrome(self, s):
        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] != s[R]:
                skipL, skipR = s[L + 1 : R + 1], s[L:R]
                return skipL == skipL[::1] or skipR == skipR[::-1]

            L += 1
            R -= 1
        return True


print(
    Solution.validPalindrome(
        None,
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
    )
)

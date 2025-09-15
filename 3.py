class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            res = max(res, r + 1 - l)

"""
increase window
keep hashmap of values found
maintain whichever value is the largest
if len - largest <= k then we can continue
repeat until k to small
return max, slide l up to r
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        for i in range(65, 91):
            window[chr(i)] = 0

        l = 0
        res = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if (r + 1 - l) - window[max(window, key=window.get)] <= k:
                pass
            else:
                # window[s[r]] -= 1
                while (r + 1 - l) - window[max(window, key=window.get)] > k:
                    window[s[l]] -= 1
                    l += 1
            res = max(r + 1 - l, res)
        return res


print(Solution.characterReplacement(None, "AABABBA", 1))

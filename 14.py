"""
This is the trie one
That's what I'm saying ^^^^^^^
No there are other answers actually
start with string at index 0
compare with string at index 1, check chars untill they don't match
move to string 2
check with prefix to see how much matches, remove if you have to
if prefix becomes 0: return empty string
"""


class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in range(1, len(strs)):
            str = strs[i]
            j = 0
            res = ""
            while j < len(str) and j < len(prefix) and prefix[j] == str[j]:
                res += prefix[j]
                j += 1
            prefix = res
        return prefix


print(Solution.longestCommonPrefix(None, ["flower", "flow", "flight"]))

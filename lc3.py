def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    r = 1
    longest = 1
    charset = set()
    charset.add(s[0])
    while r < len(s):
        if s[r] not in charset:
            charset.add(s[r])
            r += 1 #slide window
            longest = max((r-l),longest)
        else:
            charset.remove(s[l])
            l+= 1 #contract window
    return longest 
                




'''
left right pointer on 0 and 0
use set to keep track of numbers in memory
if duplicate detected, move left up and pop values from set until no more duplicates 
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        




print(lengthOfLongestSubstring('au'))

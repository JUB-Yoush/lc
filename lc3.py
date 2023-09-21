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
                

print(lengthOfLongestSubstring('au'))
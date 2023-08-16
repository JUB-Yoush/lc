def lengthOfLongestSubstring( s: str) -> int:
        hiscore = 0
        score = 1
        if len(s) == 1: return 1
        for i in range(1,len(s)-1):
            cur: int = ord(s[i])
            prev: int = ord(s[i-1])
            #sequence
            if ord(s[i]) != ord(s[i-1]):
                score += 1
            else:
                hiscore = max(hiscore,score)
                score = 1
                
        hiscore = max(hiscore,score)
        score = 1
                
        return hiscore

print(lengthOfLongestSubstring("abcabcbb"))
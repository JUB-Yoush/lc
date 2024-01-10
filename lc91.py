#https://leetcode.com/problems/decode-ways/
'''
at our current number we can
-decode single digit
-check if next digit would make a number >= 26, and decode that instead
- as cases grow we track the number of ways to record it
- is this a backtracking problem?
-0 always belongs to previous value, nothing is mapped to 0
-start at base case 1 digit
- check if next digit is a 0
- if so append that and add 0 to additional decodings (we'll return 1 + additonals)
move to next value
first digit will always add 0 additional decodings (if there is a 0 it's grouped as the first)
2nd digit will add 1 additional decoding if prev value wasn't 0 and prev + curr >= 26
2101
1123
11 23
1 1 2 3
11 2 3
1 1 23
1 12 3

12121
1 2 1 2 1
12 1 2 1
1 21 2 1
1 2 12 1
1 2 1 21
12 12 1
1 21 21
'''
class Solution:
	def numDecodings(self, s: str) -> int:
		if s[0] == '0': return 0
		additonal = 0
		for i in range(len(s)):
			if s[i] == '0':
				continue
			if i-1 < 0:
				continue
			if i+1 < len(s) and s[i+1] == '0':
				continue
			if s[i-1] == '0':
				continue
			if int(s[i-1] + s[i]) <= 26:
					additonal += 1
		return 1 + additonal
					
			


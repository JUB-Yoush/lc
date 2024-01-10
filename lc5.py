#https://leetcode.com/problems/longest-palindromic-substring/
'''
bf:
- check every substring of the string
- return longest that is a palendrome
won't work 
we need dp 
before dp, we need recursion
palins can only go up in 2s
adding one value to a palendrome would cause it to not work anymore
at least reading left to right
the base case is 1 letter
that'll be a len of 1
the other case is two letters
if it maintains palin then 
okay no dp, how would I solve
'''
#how is this dp
class Solution:
	def longestPalindrome(self, s: str) -> str:
		res = ''
		resLen = 0

		for i in range(len(s)):
			# odd len
			l,r = i,i
			while l>=0 and r < len(s) and s[l] == s[r]:
				if (r-l + 1) > resLen:
					res = s[l:r+1]
					resLen = r-l+1
				l -= 1
				r += 1
			#even len
			l,r = i,i+1
			while l>=0 and r < len(s) and s[l] == s[r]:
				if (r-l + 1) > resLen:
					res = s[l:r+1]
					resLen = r-l+1
				l -= 1
				r += 1
		return res
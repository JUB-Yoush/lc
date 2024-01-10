class Solution:
	def longestPalindrome(self, s: str) -> str:
		count = 0


		for i in range(len(s)):
			# odd len
			l,r = i,i
			while l>=0 and r < len(s) and s[l] == s[r]:
				count += 1
				l -= 1
				r += 1
			#even len
			l,r = i,i+1
			while l>=0 and r < len(s) and s[l] == s[r]:
				count += 1
				l -= 1
				r += 1
		return count
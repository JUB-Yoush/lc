#https://leetcode.com/problems/word-break/
'''
locate one dictionary word
note it and continue for the rest of the array
if array len is 0 then all the words can be fit
check for words within words?
how do we calculate all the possible divisons?
that's the question I guess
'''
class Solution:
	def wordBreak(self, s: str, wordDict) -> bool:
		wordSet = set(wordDict)
		def findword(remaining):
			if len(remaining) == 0:
				return True
			for i in range(len(remaining)):
				if remaining[:i+1] in wordSet:
					if findword(remaining[i+1:]) != False:
						return True

			return False
		return findword(s)

print(Solution.wordBreak(None,'aaaaaaa',['aaaa','aaa']))






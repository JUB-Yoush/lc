# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''
binary search... again?
I don't think anything is different
'''
class Solution:
	def firstBadVersion(self, n: int) -> int:
		l = 0
		r = n
		while True:
			m = (l+r)//2
			if isBadVersion(m) == True:
				if m == 1 or not isBadVersion(m-1): return m
				r = m -1
			else:
				l = m+1

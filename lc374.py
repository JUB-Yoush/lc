# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

'''
wait a minute I think this is just a bin search with a bit of extra fluff
l = 0 r = n
m = middle
if higher then cut out bot half
if lower then cut off top half
return
'''
class Solution:
	def guessNumber(self, n: int) -> int:
		l = 0
		r = n
		while True: #number has to exist 
			m = (l+r)//2
			if guess(m) == 0: return m
			if guess(m) == -1:
				r = m -1
			if guess(m) == 1:
				l = m+1
			
				
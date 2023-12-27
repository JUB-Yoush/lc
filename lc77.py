#https://leetcode.com/problems/combinations/
'''
at every step (while k >remaining) you can:
decrement k and pick the current number
or skip current number and decrement remaining
once k == remaining then you just need to pick the last two
if you reach the k last values
and you still have k values remaining
then you HAVE to pick them, you have no choice
chosen = 1
n = 1-4
4 - 1 = 3
'''

class Solution:
	def combine(n: int, k: int):
		subsets = []
		def pick(chosen, start):
			nonlocal subsets
			# if remaining values greater than limit
			if len(chosen) == k:
				subsets.append(chosen.copy())
				return
			for i in range(start,n+1):
				chosen.append(i)
				pick(chosen,i+1)
				chosen.pop()
		pick([],1)
		return subsets

print(Solution.combine(4,2))

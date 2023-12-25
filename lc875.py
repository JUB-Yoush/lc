import math
def minEatingSpeed(piles,h):
	
	potential_speeds = list(range(1,max(piles)+1))
	l = 0
	r = potential_speeds[-1]
	k = (r+l)//2
	found = False
	while not found:
		current_spd = potential_speeds[k]
		eat_speed = getEatingSpeed(piles,h,current_spd)
		if eat_speed == h:
			return potential_speeds[k]
		if eat_speed > h: # rm bottom half
			l = k
			k = (r+l)//2
		elif eat_speed < h: #rm top half
			r = k
			k = (r+l)//2



def getEatingSpeed(piles,h,spd):
	hours = 0
	for pile in piles:
		count = pile 
		while count > 0:
			count -= spd
			hours += 1
	return hours
	


#https://leetcode.com/problems/koko-eating-bananas/
'''
bf:
- run through every potential banana eat speed and see which one takes h hours?
the h is a hard limit
can't be slower than that
however we want to find the integer that is closest to it
binary search is involved, 
what is the range of numbers we're looking through
NO IT'S NOT
the fastest koko could eat all bananas is the amount of piles there are
even if she could eat 9999999 bananas per hour she eats one pile at a time
so k >= h
so minimum k can start at h?
which would be too slow to complete
finding the lowest time that completes is the point of this problem
k is a range of h - unbounded
we can't do a binary search unless we know the range
but it dosen't have to be the range of values that work
h can be too slow
so h2 could be too fast?
the max pile length is 10^4
so h - 10^4?
h2 would be the max of one of the piles right?
yeah 
testcase: piles = [3,6,7,11], h = 8
range = 4 - 11 bananas per hour
eat speed = 7
3 -> 0
6 -> 0
7 -> 0
11 -> 4 -> 0
total: 5 hours
5 is less than 8
we can eat bananas slower
range: 4 - 7
eat speed = 5
3 -> 0
6 -> 1 -> 0
7 -> 2 -> 0
11 -> 6 -> 1 -> 0
== 8
yipee good eat number found
this question aint that bad

test case: piles = [3,6,7,11], h = 8

'''
class Solution:
	def minEatingSpeed(piles, h) -> int:
		def simulate_eat_speed(bph):
			hours = 0
			i = 0
			sim_pile = piles.copy()
			while i < len(sim_pile):
				hours += 1
				sim_pile[i] = max(0,sim_pile[i] - bph)
				if sim_pile[i] == 0: i+= 1
			return hours

				
			

		l = len(piles)
		r = max(piles)
		res = 0
		while l<=r:
			m = (l+r)//2
			eat_speed = 0
			#eat_speed = simulate_eat_speed(m)
			for p in piles:
				eat_speed += math.ceil(float(p)/m)
			if eat_speed <= h:
				res = m
				r = m -1
			if eat_speed > h:
				l = m+1
		return res



print(Solution.minEatingSpeed([30,11,23,4,20],5)) 
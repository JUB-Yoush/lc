#https://leetcode.com/problems/insert-interval/
'''
interval insertion
loop through every interval
check if curr_invterval overlaps the new interval
if it does, pick the min and max of intervals to make a new one
but we should also check first to make sure that the interval can't just fit normally.
how do we know if an interval can fit normally?
if lower[1] < higher[0] # lower one ends before higher one begins
we'd also need to check in front of it to make sure that one isn't overlapping
maybe we could insert it as we find it
what is the issue I'm running into
I need to check ahead of it but also behind it
just those two cases?
I think so
so check interval behind, see if it fits
check interval in front, see if it fits
if not to either, merge it and return
if it does fit, return
'''

class Solution1:
	def insert(self, intervals, newInterval):
		for i,interval in enumerate(intervals):
			# if fit behind and fit in-front
			#bigger = None
			#smaller = None
			#if interval[0] > newInterval[0]:
				#bigger = interval
				#smaller = newInterval
			#else:
				#bigger = newInterval
				#smaller = interval
			#if smaller[1] < bigger[0]
			pass



# neetcode soln
class Solution:
	def insert(self, intervals, newInterval):
		res = []
		for i in range(len(intervals)):
			if newInterval[1] < intervals[i][0]:
				res.append(newInterval)
				return res + intervals[i:]
			elif newInterval[0] > intervals[i][1]:
				res.append(intervals[i])
			else:
				newInterval = [
					min(newInterval[0],intervals[i][0]),
					max(newInterval[1],intervals[i][1])
				]
		res.append(newInterval)
		return res

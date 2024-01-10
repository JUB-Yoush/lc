"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
'''
hey hey! I know this one
you want to put them in a binary search tree, and check if every new value can be properly inserted
both start and end need to be less than or greater than the other start and end
no lmao
what you do is you sort them, then loop through them and check for overlaps (end of last one greater then start of current)
if no overlaps then it's fine
'''

class Solution:
	def canAttendMeetings(self, intervals: List[Interval]) -> bool:
		intervals.sort(key=lambda i: i[0])
		for i in range(1,len(intervals)):
			i1 = intervals[i-1]
			i2 = intervals[i]

			if i1[1] > i2[0]:
				return False
		return True


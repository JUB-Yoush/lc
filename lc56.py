#https://leetcode.com/problems/merge-intervals/description/
'''
treat intervals as pairs
or loop from 2nd and count previous
check if the lower interval end is less then bigger interval start
    wait are the intervals sorted?
if so then form new interval of min start max end 
more then one interval can get grouped together
don't just assume interval has been solved after the one
rnd 2
sort!!
okay check interval one and interval 2
if they overlap merge, 
if they don't overlap, then append interval 1 to output
repeat until only 1 interval remaining
'''

class Solution:
    def merge(self,intervals):
        intervals.sort(key=lambda i: i[0])
        res = []
        i = 1
        while len(intervals) > 1:
            a = intervals[0]
            b = intervals[1]
            # improper interval: fuse
            if intervals[0][1] >= intervals[1][0]:
                new_interval = [min(intervals[0][0],intervals[1][0]),max(intervals[0][1],intervals[1][1])]
                intervals.pop(0)
                intervals.pop(0)
                intervals.insert(0,new_interval)
            else:
                res.append(intervals.pop(0))
        res.append(intervals.pop(0))
        return res
        
        



print(Solution.merge(None,[[1,3],[2,6],[8,10],[15,18]]))
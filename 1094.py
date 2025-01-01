from collections import defaultdict
"""
sort input by from
keep a queue to manage the end times of trips
once we reach a start time past the end time, remove those passengers from the car
"""
"""
class Solution:
    def carPooling(self, trips, capacity):
        queue = []
        invervals = {}
        riders = 0
        # sort by start time
        trips = sorted(trips, key=lambda x: x[1])
        i = 0
        while trips:
            while trips and trips[0][1] == i:
                # if we've reached the stop, add to queue
                t = trips[0]
                queue.append([t[2],t[0]])
                riders += t[0]
                trips.pop(0)
            # end old rides
            while queue and i == queue[0][0]:
                riders -= queue[0][1]
                queue.pop(0)
            if riders > capacity:
                return False
            i+= 1
        return True
"""

class Solution:
    def carPooling(self, trips, capacity):
        starts = sorted(trips, key=lambda x: x[1])
        ends = sorted(trips, key=lambda x: x[2])
        riders = 0
        i = 0
        while starts:
            while starts and starts[0][1] == i:
                riders += starts[0][0]
                starts.pop(0)
            while ends and ends[0][2] == i:
                riders -= ends[0][0]
                ends.pop(0)
            if riders > capacity:
                return False
            i+= 1
        return True



print(Solution.carPooling(None,[[3,2,8],[4,4,6],[10,8,9]],11))
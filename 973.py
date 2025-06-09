"""
distances and positions are related to each other, mapped even.
use a hashmap that stores distances and locations
dist:[points]
then loop through and pop the closest
can't loop through arrays in a sorted order
can't find the time complexity for sorted() rather lol
doing that is probably fine
wait I turned it into a heap I'm kinda goated.
wait wait, I could've just sorted the list
building is n put poping is logn
doing logn action n times is n * logn
so it's the same as nlogn and n
"""

import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pointmap = {}
        for point in points:
            x = point[0]
            y = point[1]
            euclid = math.sqrt((x**2) + (y**2))
            if euclid not in pointmap:
                pointmap[euclid] = []
            pointmap[euclid].append([x, y])

        keys = list(pointmap.keys())
        keys.sort()
        res = []
        i = 0
        while k > 0:
            while pointmap[keys[i]]:
                res.append(pointmap[keys[i]].pop())
                k -= 1
            i += 1
        return res


print(Solution.kClosest(None, [[3, 3], [5, -1], [-2, 4]], 2))

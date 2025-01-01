# 1046. Last Stone Weight
import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
            stones = [-x for x in stones]
            heapq.heapify(stones)
            while len(stones) > 1:
                heapq.heappush(stones,(heapq.heappop(stones) - heapq.heappop(stones)))
               # if heapq.heappop(stones) != 0:
               #     heapq.heappush(stones,)
               # pass

            if len(stones) == 1:
                return -1*stones[0]
            return 0

print(Solution.lastStoneWeight(None,[2,7,4,1,8,1]))
"""
8-7

"""
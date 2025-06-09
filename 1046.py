import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
        if stones:
            return heapq.heappop(stones)
        return 0

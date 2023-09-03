import heapq
def lastStoneWeight(stones: list[int]) -> int:
        # turn values negative so it'll be a max-heap instead of a min-heap
        negstones = [-x for x in stones]
        heapq.heapify(negstones) 
        while len(negstones) > 1:
            big1 = (heapq.heappop(negstones)) * -1
            big2 = (heapq.heappop(negstones)) * -1
            output = big1 - big2
            if output > 0: # if the remainder isn't 0, add it back to the heap
                heapq.heappush(negstones,-output)
        return negstones[0] *-1

print(lastStoneWeight([2,7,4,1,8,1]))

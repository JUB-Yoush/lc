import heapq
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k) -> int:
        prices = {}
        adj_list = []
        for i in range(n):
            adj_list.append([])
        shortest_path = {}
        for flight in flights:
            adj_list[flight[0]].append((flight[1],flight[2],1))
        # cost,node,number of trips
        min_heap = [[0,src,1]]
        while min_heap:
            w1, n1, f1 = heapq.heappop(min_heap)
            if n1 in shortest_path or f1 > k+2:
                continue
            shortest_path[n1] = w1

            for (n2, w2, f2) in adj_list[n1]:
                if n2 not in shortest_path:
                    heapq.heappush(min_heap, [w1 + w2,n2,f1+f2])
        if dst not in shortest_path:
            return -1
        return shortest_path[dst]


print(Solution.findCheapestPrice(None,4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))





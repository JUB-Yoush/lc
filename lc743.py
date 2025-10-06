from collections import defaultdict, deque
import heapq
# https://leetcode.com/problems/network-delay-time/description/


class Solution:
    def networkDelayTime(self, times, n: int, k: int):
        # make graph
        edges = defaultdict(list)
        visited = set()
        all = set()

        for u, v, w in times:
            edges[u].append((v, w))
            all.add(u)

        # start pathfinding from k
        min_heap = []
        min_heap.append((k, 0))
        time = 0

        while min_heap:
            curr_node, curr_time = heapq.heappop(min_heap)
            if curr_node in visited:
                continue

            visited.add(curr_node)
            time = max(time, curr_time)

            for neighbor, dist in edges[curr_node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor, curr_time + dist))
        return time if len(visited) == n else -1

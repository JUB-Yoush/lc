from collections import deque
import heapq
#https://leetcode.com/problems/network-delay-time/description/
'''
we're given a source node
and need to manage the shortest path from that node to every other node?
so we need to check when every node has been visited
implement shortest path algorithm and return the largest value 
'''
class Solution1:
		def networkDelayTime(self, times, n: int, k: int):

			adj_list = [[]] * n + 1 
			for time in times:
				adj_list[time[0]].append((time[1],time[2]))

			min_heap = []

			# start node
			shortest = {}
			heapq.heappush(min_heap,(k,0))
			while min_heap:
				# weight and node
				w1,n1 = heapq.heappop(min_heap)

				if n1 in shortest:
					continue

				shortest[n1] = w1

				for n2, w2 in adj[n1]:
					if n2 not in shortest:
						heapq.heappush(min_heap,[w1+w2,n2])
			min_time = 0
			for short in shortest:
				min_time = max(min_time,short)
			return min_time
			
import collections
# neetcode
class Solution:
		def networkDelayTime(self, times, n: int, k: int):
			edges = collections.defaultdict(list)

			for u,v,w in times:
				edges[u].append((v,w))
			
			min_heap = [(0,k)]
			visit = set()
			t = 0
			while min_heap:
				w1,n = heapq.heappop(min_heap)
				if n1 in visit:
					continue
				visit.add(n1)
				t = max(t,w1)

				for n2,w2 in edges[n1]:
					if n2 not in visit:
						heapq.heappush(min_heap,(w1+w2,n2))
			return t if len(visit) == n else -1




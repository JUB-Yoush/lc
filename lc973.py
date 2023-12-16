#https://leetcode.com/problems/k-closest-points-to-origin/description/
"""
what
this seems like the k frequent elements problem but with heaps for real this time no array hacking
using the euclidean distance is LAME i mean easy because the other value is always 0
so it's just sqrt(x^2 + y^2)
calculate the distances of each, put in an array
convert to heap
pop top k heap elems
we have to return the point, not the distance
this is hard because two points can have the same distance
how do I store the points within the heap???
make it a 3rd index lol
make the distance the key, value is an array of every point of that distance
heap sorted by keys (dist)
pop value and check how many children it has
push k kids
"""
import heapq
class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		# make funny hashmap [DISTANCE:[POINT_AT_DISTANCE]]
		# it's a sub-array because multiple points can have the same dist
		distances = {}
		for point in points:
			#distances.append(sqrt(point[0]**2 + point[1]**2))
			distance = sqrt(point[0]**2 + point[1]**2)
			if distance not in distances:   
				distances[distance] = []
			distances[distance].append(point)
		distance_keys =list(distances.keys()) 

		# make list of keys and sort as a heap 
		heapq.heapify(distance_keys) 
		kids_pushed = 0
		output = []
  
		# pop the top k kids by popping the top element and adding all it's kids
		while kids_pushed < k:
			closest_dist = heapq.heappop(distance_keys)
			for kid in distances[closest_dist]:
				output.append(kid)
				kids_pushed += 1
				if kids_pushed == k:
					break
		return output
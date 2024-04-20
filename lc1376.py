#https://leetcode.com/problems/time-needed-to-inform-all-employees/
'''
it's a BFS, with different amounts of distance between nodes?
we can use the manager list to build out the tree
have an array that manages the time the report was sent out to that node
start at the head
find all nodes that report to the head
make their report time parent_report_time + report time 
add them to a queue
repeat till queue empty


'''
from collections import deque
class Solution:
	#class Employee:
		#def __init__(self,informTime,parent)
	def numOfMinutes(self, n: int, headID: int, manager , informTime) -> int:
		longest_msg_time = 0
		queue = deque()
		got_msg = [0] * len(manager)

		adj_list = {}
		for i,m in enumerate(manager):
			if m == -1:
				continue
			if m not in adj_list:
				adj_list[m] = []
			adj_list[m].append(i)

		queue.append(headID)
		while queue:
			for i in range(len(queue)):
				employee = queue.popleft()
				if employee not in adj_list:
					continue
				for gopher in adj_list[employee]:
					got_msg[gopher] = got_msg[employee] + informTime[employee]
					longest_msg_time = max(longest_msg_time, got_msg[gopher])
					queue.append(gopher)
		
		return longest_msg_time


print(Solution.numOfMinutes(None,6,2,[2,2,-1,2,2,2],[0,0,1,0,0,0]))
'''
we want to cut it in a way that makes it a tree
we'd have to pick which node we'd want to be the root
we're just removing any cycles right?
first we'd have to detect a cycle
then find the values
fast and slow algorithm
just use a visited set
assemble graph based on edges
manage node you just left, don't go back and forth
if you reach a node already in visited, remove the last connection?
nodes are labeled 1-n, can use an array to store them
start at 1 and traverse list in dfs
if ever return to 1 then remove last node you were at from list
how do I get the answer that occurs last?
start from highest node, then go to lowest nodes
seems like that works?
'''
class Solutionfake:
	def findRedundantConnection(self, edges):

		def dfs(visited,curr_node,prev_node):
			nonlocal graph
			for edge in graph[curr_node]:
				if edge in visited:
					continue
				visited.add(edge)
				return dfs(visited,edge,curr_node)
			#if we break out then there were no values to loop over	
			return [edge,curr_node]

		n = 0
		for edge in edges:
			#find max value (1-indexed)
			n = max(n,edge[0],edge[1])
		
		graph = [[] for _ in range (n+1)]
		#build graph (undirected)
		for edge in edges:
			graph[edge[0]].append(edge[1])
			graph[edge[1]].append(edge[0])
		'''
		1:2,4,5
		2:3,1
		3:4,2
		4:1,3
		5:1
		'''
		for i in range(len(graph)-1,0,-1):
			visited = set()	
			visited.add(i)	
			return dfs(visited,i,None)



class Solution:
	def findRedundantConnection(self, edges):
		

print(Solution.findRedundantConnection(None,[[1,2],[2,3],[3,4],[1,4],[1,5]]))		





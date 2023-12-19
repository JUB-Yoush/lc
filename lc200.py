#https://leetcode.com/problems/number-of-islands/
'''
recursive check?
go to each 1, check if all neighbors are water
if not then it's connected
if it is then it's an island and uhhhh
how do we check for other islands afterwards
considering this is a fundamental problem looking at how these things are solved would be fine ig
so it's as I thought
start at 0,0
if 1, check if not already part of island
loop through and find connecting (manage found pieces in a list of some kind?)
once all the pieces have been found, label it as an island
traverse 0s to eventually reach other 1s
but how to manage the 1s we've already reached?
change it to 2?
'''
#neetcode soln
class Solution:
	def numIslands(self, grid) -> int:
		if not grid:
			return 0
		rows, cols = len(grid),len(grid[0])
		visit = set()
		islands = 0
		
		# iterative bfs
		#use a set to manage visited island
		def bfs(r,c):
			q = collections.deque()
			visit.add((r,c))
			q.append((r,c))

			while q:
				row,col = q.popleft()
				direction = [[1,0],[-1,0],[0,1],[0,-1]]
				for dr,dc in direction:
					r,c = row+dr, col+dc
					if (r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in visit):
						q.append((r,c))
						visit.add((r,c))
		
		
		
		for r in range (rows):
			for c in range(cols):
				if grid[r][c] == '1' and (r,c) not in visit:
					bfs(r,c)
					islands += 1
		return islands
				
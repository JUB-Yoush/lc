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
				






'''
redo-ing to verify comprehension
question is asking ability to traverse a graph
how would a 5 year old solve this
just circle the islands
how do we "cirlce" an island?
start at 00
if list index oob then assume it's water
store if visited in a tuple with index and then if it was visited?
or just change it from a 1 to a 2?

'''
class Solution2:
	def numIslands(grid) -> int:

		def search(col,row):
			nonlocal grid
			grid[col][row] = '2'
			#up
			if col -1 >= 0 and grid[col-1][row] == '1':
				search(col-1,row)
			#left
			if row -1 >= 0 and grid[col][row-1] == '1':
				search(col,row-1)
			#down
			if col +1 < len(grid) and grid[col+1][row] == '1':
				search(col+1,row)
			#right
			if row +1 < len(grid[0]) and grid[col][row+1] == '1':
				search(col,row+1)
		islands = 0
		for col in range(len(grid)):
			for row in range(len(grid[0])):
				if grid[col][row] == '1':
					search(col,row)
					islands += 1
		return islands

print(Solution2.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))


'''
review:
loop through tiles
mark visited tiles in visited set 
if tile is island then dfs
'''
class Solution3:
	def numIslands(self, grid):
		
		pass
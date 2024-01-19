#https://leetcode.com/problems/max-area-of-island/
'''
it's a bfs (or dfs ig) of the islands
loop through the grid and check if an tile is a 1
have a visted set() or change it to 2 if we're able to modify the graph
collect the max_area
it'd have to be a breadth first search because we'd run into corners
wait if we just pass up if we're another island tile or not I think a dfs would work fine
'''
class Solution1:
	def maxAreaOfIsland(self,grid):
		ROWS,COLS = len(grid), len(grid[0])
		visited = set()
		max_area = 0
		def dfs(r,c):
			# if not a new island tile (or oob)
			if (r,c) in visited or min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
				return 0
			visited.add((r,c))
			return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)

		for r in range(len(grid)):
			for c in range(len(grid)):
				if grid[r][c] == 1 and (r,c) not in visited:
					area = dfs(r,c)
					max_area = max(area,max_area)
		return max_area



'''
loop thru every tile
if tile is a 1 then start dfs
return the size of the island by adding 1 + dfs all directions
if largest then update
return largest
'''
class Solution:
	def maxAreaOfIsland(self, grid):
		visited = set()
		DIRECTIONS = [[-1,0],[0,1],[1,0],[0,-1]]
		max_island = 0
		ROWS = len(grid)
		COLS = len(grid[0])

		def dfs(r,c):
			if (r,c) in visited or min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
				return 0
			visited.add((r,c))
			neighbor_size = 0
			for dir in DIRECTIONS:
				neighbor_size += dfs(r+dir[0],c+dir[1])
			return 1 + neighbor_size


		for r in range(ROWS):
			for c in range(COLS):
				island = 0
				if grid[r][c] == 1:
					island = dfs(r,c)
					max_island = max(max_island,island)
		return max_island



print(Solution.maxAreaOfIsland(None,[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
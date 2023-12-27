#https://leetcode.com/problems/max-area-of-island/
'''
it's like the other island question but we keep track of the islands we've visited
'''
class Solution:
	def maxAreaOfIsland(self,grid):
		curr_area = 0
		def search(col,row):
			nonlocal grid
			nonlocal curr_area
			grid[col][row] = 2
			curr_area += 1
			#up
			if col -1 >= 0 and grid[col-1][row] == 1:
				return 1 + search(col-1,row)
			#left
			if row -1 >= 0 and grid[col][row-1] == 1:
				return 1 + search(col,row-1)
			#down
			if col +1 < len(grid) and grid[col+1][row] == 1:
				return 1 + search(col+1,row)
			#right
			if row +1 < len(grid[0]) and grid[col][row+1] == 1:
				return 1 + search(col,row+1)
			else:
				return 1
		max_area = 0
		for col in range(len(grid)):
			for row in range(len(grid[0])):
				if grid[col][row] == 1:
					search(col,row)
					max_area = max(max_area,curr_area)
					curr_area = 0
		return max_area

print(Solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
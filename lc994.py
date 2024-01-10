from collections import deque
#https://leetcode.com/problems/rotting-oranges/
'''
sad oranges
it's a bfs over a grid
so try to remember the steps for that
how to bfs over a grid:
- define m and n as constants rows and cols
- make a queue and a set to track neighbors and visited
- add initial values? (in this case it'd be all already rotten oranges? or do we just pick one)
- loop until queue empty
- check if:
	- next is within bounds
	- next is a fresh orange
	- if next is a rotten orange then add to queue
- I think the challenge of this question comes from there not being one place the rotten oranges start at
- usually a bfs of a graph expands outwards from an initial point, making it easy to track time elapsed between generations
- but they're all moving at the same time?
- some oranges are going to double rot an orange?
bf:
	- loop through every single space to see how each orange has changed
	- that would be an (n*m)^2 operation 

maybe we could have two alternating queues
one queue to start, and another queue that is the next wave of oranges rotted
during the current wave, add any newly rotted oranges to the next wave
then loop over that wave
once the next wave is empty, we know we've looped over everything
return time

xxo
xo-
-oo
queue = [[1,0],[0,2],[1,1]]
visited = [(0,0),(0,1),(1,0)]
1
0,1
'''
class Solution:
	def orangesRotting(grid):
		ROWS,COLS = len(grid), len(grid[0])
		time = -1
		visited = set()
		queue = deque() # currently looping over

		# edge case: no oranges
		has_orange = False
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] != 0:
					has_orange = True

		if not has_orange:
			return -1

		
		# find all inital rotten oragnges
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] == 2:
					queue.append((row,col))
					visited.add((row,col))
				

		while queue:
			for i in range(len(queue)):
				r,c = queue.popleft()
				neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
				for dr,dc in neighbors:
					# if not (within bounds and a new fresh orange)
					if min(r+dr,c+dc) < 0 or r + dr == ROWS or c + dc == COLS or (r+dr,c+dc) in visited or grid[r+dr][c+dc] == 0:
						continue
					queue.append((r+dr,c+dc))
					visited.add((r+dr,c+dc))
			time += 1

		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if (row,col) not in visited and grid[row][col] != 0:
					return -1
		return time

print(Solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))



from collections import deque
'''
breadth first search on a matrix
how does I do that
have a queue to keep track of neighbor nodes I've visited
iterate time after all the neighbors have been visited
'''
class Solution:
	def orangesRotting(self,grid):
		ROWS, COLS = len(grid), len(grid[0])
		visited = set()
		queue = deque()
		minutes = 0
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c] == 2:
					queue.append((r,c))
					visited.add((r,c))

		while queue:
			for i in range(len(queue)):
				r,c = queue.popleft()
				neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
				for n in neighbors:
					r,c = r+n[0], c+n[1]
					#fresh orange within bounds
					if r < ROWS and c < COLS and min(r,c) > -1 and grid[r][c] == 1:
						queue.append((r,c))
						grid[r][c] = 2
			if len(queue) > 0:
				minutes += 1
				
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c] == 1:
					return -1

		return minutes

					

import collections
#https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''
make queue of positions, start at 0,0
have two loops, one that loops while the queue is full and one that loops for all the values it's checking
once interior loop ends, increase length
'''
class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

		ROWS, COLS = len(grid), len(grid[0])
		visited = set()
		queue = collections.deque()
		queue.append((0,0))
		visited.add((0,0))
		length = 0

		while queue:
			for i in range(len(queue)):
				r,c = queue.popleft()
				# rows and cols are the same, the grid is nxn
				# in bounds, not 1, not visited
				if(min(r,c) < 0 or max(r,c) >= ROWS or grid[r][c] == 1 or (r,c) in visited):
					continue
				# if at goal
				if r == ROWS -1 and c == COLS -1:
					return length

				neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
				for dr,dc in neighbors:
					if(min(r,c) < 0 or max(r,c) >= ROWS or grid[r][c] == 1 or (r,c) in visited):
						queue.append((r+dr,c+dc,length +1))
						visited.add((r+dr,c+dc))
		return -1
					

# neetcode ver
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, length
        visit = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= N or
                grid[r][c]):
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1


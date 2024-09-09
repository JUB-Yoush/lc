#https://leetcode.com/problems/rotting-oranges/description/
from collections import deque
"""
bfs
make sure there are fresh oranges to begin with (if no fresh oranges then )
add fresh oranges to queue,
rot them, find fresh oranges next to them
repeat until done
keep track of iterations
"""
class Solution:
    def orangesRotting(self, grid):
        time = 0
        freshies = 0
        queue = deque()
        DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
        # collect rotten ones
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])
                elif grid[r][c] == 1:
                    freshies += 1
        if freshies == 0:
            return 0

        while queue:
            prev_freshies = freshies
            for i in range(len(queue)):
                orange = queue.popleft()
                for dir in DIRECTIONS:
                    r = orange[0] + dir[0]
                    c = orange[1] + dir[1]
                    if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                        continue
                    queue.append([r,c])
                    grid[r][c] = 2
                    freshies -= 1
            if freshies != prev_freshies:
                time+= 1

        if freshies == 0:
            return time
        else:
            return -1



print(Solution.orangesRotting(None,[[2,1,1],[1,1,0],[0,1,1]]))



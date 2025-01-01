"""
moving diagonally is always faster than moving cardinally, so check diagonally first
return distance
0000
1110
0001
0111
"""
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        minlen = float('inf')

        DIRS = ((1,1),(1,-1),(-1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1))
        visited = set()

        # x,y,length
        queue.append((0,0,0))

        while queue:
            for i in range(len(queue)):
                r,c,l = queue.popleft()

                if (r,c) == (ROWS-1,COLS-1):
                    minlen = min(minlen,l)


                for x,y in DIRS:
                    new_r = r+x
                    new_c = c+y
                    if min(new_r,new_c) < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] == 1 or (new_r,new_c) in visited:
                        continue

                    visited.add((new_r,new_c))
                    queue.append((new_r,new_c,l+1))
        if minlen == float('inf'):
            return -1
        return minlen

print(Solution.shortestPathBinaryMatrix(None,[[1,0,0],[1,1,0],[1,1,0]]))
#https://leetcode.com/problems/number-of-islands/description/
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        have a list of visited 1s
        if 1 isn't visited, start a dfs and visit all the ones around it
        increase island count
        """
        visit = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c,visit):
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == "0"):
                return
            visit.add((r,c))
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)

        for r in range(ROWS):
            for c in range(COLS):
                if (min(r,c) > 0 and r < ROWS and c < COLS and (r,c) not in visit and grid[r][c] == "1"):
                    dfs(r,c,visit)
                    islands += 1
        return islands

print(Solution.numIslands(self,[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))





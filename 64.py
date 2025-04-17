"""
start at 0,0
check pick from self + min of right and self + min of down
repeat until you reach r,c
return 0,0
"""


class Solution:
    def minPathSum(self, grid):
        memo = {}
        ROWS = len(grid)
        COLS = len(grid[0])
        memo[(ROWS - 1, COLS - 1)] = grid[ROWS - 1][COLS - 1]

        def pick(r, c):
            right_pick = float("inf")
            down_pick = float("inf")
            if (r, c) in memo:
                return memo[(r, c)]

            if r != ROWS - 1:
                right_pick = pick(r + 1, c)

            if c != COLS - 1:
                down_pick = pick(r, c + 1)

            memo[(r, c)] = grid[r][c] + min(right_pick, down_pick)
            return memo[(r, c)]

        pick(0, 0)
        return memo[(0, 0)]

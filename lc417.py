# https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
It's a dfs
find all tiles that can reach pac, find all tiles that can reach atl
find the intersection of both sets and return that
you can figure out if a tile can reach an ocean by starting at an edge and dfsing every edge that can be flown from (check if it has a larger height)
simple really
"""


class Solution:
    def pacificAtlantic(self, heights):
        def reaches(r, c, target_set, prev_height):
            # invalid cell (oob or can't flow)
            if (
                (r, c) in target_set
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prev_height
            ):
                return

            target_set.add((r, c))

            for dir in DIRS:
                dr = r + dir[0]
                dc = c + dir[1]
                reaches(dr, dc, target_set, heights[r][c])

        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(heights)
        COLS = len(heights[0])
        reach_pac = set()
        reach_atl = set()

        # dfs starting from edges
        for c in range(COLS):
            reaches(0, c, reach_pac, heights[0][c])
            reaches(ROWS - 1, c, reach_atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            reaches(r, 0, reach_pac, heights[r][0])
            reaches(r, COLS - 1, reach_atl, heights[r][COLS - 1])

        # get intersection of atl and pac sets
        return list(reach_pac & reach_atl)

"""
find island (search algo)
if I have a neighbour on a side, don't count that face
sides that are oob with no neighbour count too
"""


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1],
        ]
        edges = 0

        visited = set()

        def dfs(r, c):
            nonlocal edges

            # oob or not island tile:
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                edges += 1
                return

            if (r, c) in visited:
                return

            visited.add((r, c))

            # dfs on neighbours
            for dir in DIRS:
                dr = dir[0]
                dc = dir[1]
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
        return edges


print(
    Solution.islandPerimeter(
        None, [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    )
)

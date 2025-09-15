class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        self.prefix = [[0 for _ in range(cols)] for _ in range(rows)]
        # self.prefix[0].append([0 for i in range(len(matrix[0]))])

        for r in range(1, rows):
            for c in range(1, cols):
                self.prefix[r][c] = (
                    matrix[r - 1][c - 1] + self.prefix[r - 1][c] + self.prefix[r][c - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]
        topLeft = self.prefix[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(
    [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
)
param_1 = obj.sumRegion(2, 1, 4, 3)

"""
one queen can only exist on every row, col, and diag
diagonals can either be counted positivley or negativley
pos diag nav: r + 1 c + 1
neg diag nav: r-1 c + 1
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []

        def backtrack(board, queens):
            if len(queens) == n:
                res.append(board.copy())

            pass

"""
Queens can't share a row, col, or diag
loop row by row
maintain the columns you've already used
maintain the diagonal we're on using r -c for neg ones, and r+c for positive
"""


class Solution:
    def solveNQueens(self, n):
        cols = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        board = [["."] * n for i in range(n)]
        # loop over every row

        def place(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                # try placing a queen in a spot
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = "Q"

                place(row + 1)

                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = "."

        place(0)
        return res

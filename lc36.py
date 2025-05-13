"""
what I remember:
- treat the problem like a 3x3 grid
- rows and cols unqiue isn't super hard, just make a set n check
- nvm we should use a hashset I guess.
- checking the squares is the hard part
- use modulo and loop over each section?
- array slicing?
- just have sets of ranges, loop over them
"""


class Solution:
    def isValidSudoku(self, board) -> bool:
        def valid_subgrid(r_range, c_range):
            subset = set()
            for r in r_range:
                for c in c_range:
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in subset:
                        return False
                    subset.add(board[r][c])
            return True

        SUBGRID_RANGES = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        ROWS = 9
        COLS = 9

        for r_range in SUBGRID_RANGES:
            for c_range in SUBGRID_RANGES:
                if not valid_subgrid(r_range, c_range):
                    return False

        # check rows
        for r in range(ROWS):
            rowset = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowset:
                    return False
                rowset.add(board[r][c])

        # check cols
        for c in range(COLS):
            rowset = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowset:
                    return False
                rowset.add(board[r][c])

        return True


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]

sol = Solution()
print(Solution.isValidSudoku(sol, board))

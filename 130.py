"""
go along the edges, collect all Os
run a dfs from every O, to every O it can reach
all the other Os are captured
loop through and update board, return it

"""
class Solution:
    def solve(self, board) -> None:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r,c):
            if (
                (r,c) in visited
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] == "X"
            ):
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)

        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = "X"

        return board
Solution.solve(None,[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])
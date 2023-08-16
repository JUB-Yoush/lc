def isValidSudoku(board: list[list[str]]) -> bool:
    # make dictonaries to find duplicates
   cols = collections.defualtdict(set)
   rows = collections.defualtdict(set)
   squares = collections.defaultdict(set)

    # loop over every cell
    for i in range(9):
        for c in range(9):
            #skip .s
            if board[r][c] == ".":
                continue
            #check if the current value is already in a dict we have
            if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                return False
            #if not add value to dict
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])

        


        


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))        
        
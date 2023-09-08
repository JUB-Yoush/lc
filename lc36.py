
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
            squares[r//3,c//3].add(board[r][c])
    return True

        



    
    '''
    # find a way to group the 3x3's pass into hashset check

    # for each row hash set check
    for row in board:
        hset = set()
        for num in row:
            if num in hset:
                return False
            hset.add(num)
            
    # for each col hashset check
    for i in range(0,len(row)):
        hset = set()
        for row in board:
            if row[i] in hset:
                return False
            hset.add(row[i])
    
    dquares = collections.defaultdict(set)

        
        

    

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))        
'''
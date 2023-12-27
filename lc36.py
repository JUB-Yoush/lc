
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

        



    

#https://leetcode.com/problems/valid-sudoku/
'''
what do I remember:
somthing about treating the entire board as a 3x3 grid
and the 3x3 grids somthing somthing on the inside
yep
it's jover
'''
class Solution:
    def isValidSudoku(self, board):
        # check rows
        for col in range(9):
            row = board[col]
            row_set = set()
            for num in row:
                if num == '.': return
                if num != '.' and int(num) in row_set:
                    return False
                row_set.add(int(num))
                
        # check columns
        col_set = set()
        for i in range(9):
            col_set = set()            
            for col in board:
                num = col[i]
                if num == '.': 
                    return
                if num != '.' and int(num) in col_set:
                    return False
                col_set.add(int(num))

        # check 3x3s
        # 0-2 3-5 6-8
        sub_board_sections = [[0,1,2],[3,4,5],[6,7,8]]
        for sectionx in sub_board_sections:
            for sectiony in sub_board_sections:
                subset = set()
                for x in sectionx:
                    for y in sectiony:
                        num = board[y][x]
                        if num == '.': 
                            return
                        if num != '.' and int(num) in col_set:
                            return False
                        subset.add(int(num))
        return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))        

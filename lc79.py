#https://leetcode.com/problems/word-search/
'''
this smells like a dfs
loop all values
if first letter matches then run dfs to find word snake
'''
class Solution:
	def exist(self, board, word: str) -> bool:
		ROWS,COLS = len(board),len(board[0])
		DIRECTIONS = [[0,-1],[0,1],[-1,0],[1,0]]
	
		def dfs(r,c,i,pathset) -> int:
		# if new tile within bounds that matches our letter
			if not min(r,c) < 0 or r == ROWS or c == COLS:
				if ( i == len(word) or board[r][c] != word[i]): 
					return 0
				if len(word)-1 == i: 
					return 1
				for dir in DIRECTIONS:
					new_r,new_c = r+dir[0],c+dir[1]
					if ((new_r,new_c)) not in pathset:
						pathset.add((new_r,new_c))
						return 0 + dfs(new_r,new_c,i+1,pathset)
			return 0

		for r in range(ROWS):
			for c in range(COLS):
				if board[r][c] == word[0]:
					pathset = set()
					pathset.add((r,c))
					found = dfs(r,c,0,pathset)
					if found > 0: return True
		return False
		

print(Solution.exist(None,[["A","B","C","E"],
                           ["S","F","C","S"],
                           ["A","D","E","E"]],"ABCCED"))


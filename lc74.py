def searchMatrix(matrix: list[list[int]], target: int) -> bool:
	# do binary search on leftmost column to find out which row to check 
	max_row = len(matrix[0])-1
	high = len(matrix) -1
	low = 0
	answer_row = []
	while True:
		center = len(matrix) -1 //2
		if matrix[center][0] == target:
			return True
		if matrix[center][0] <
		if matrix[center][0] > target:
			center 
		elif matrix[center][0] > target and matrix[center][max_row] < target:
			answer_row = matrix[center]
			

#https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
	def searchMatrix(matrix,target):
		def binsearch(row):
			nonlocal target
			l = 0
			r = len(row) -1
			while l<=r:
				m = l+ (r-l) //2
				if row[m] == target:
					return True
				if row[m] < target:
					l = m +1
				elif row[m] > target:
					r = m-1
			return False

		l = 0
		r = len(matrix) -1
		while l<r:
			m = (r+l) //2
			# if value exists, it's in this row
			if matrix[m][0] < target and matrix[m][-1] > target:
				return binsearch(matrix[m])
			if matrix[m][0] > target:
				r = m 
			elif matrix[m][0] < target:
				l = m 

			

print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))

def searchMatrix(self,matrix,target):
	# neetcode
	ROWS, COLS = len(matrix), len(matrix[0])
	top, bot = 0, ROWS -1

	while top <= bot:
		row = (top + bot) //2
		if target > matrix[row][-1]:
			top = row +1
		elif target < matrix[row][0]:
			bot = row +1
		else:
			break
		if not(top <= bot): return False
		row = (top + bot)//2
		l,r = 0,COLS -1
		while l<= r:
			m = (l+r) //2
			if target > matrix[row][m]:
				l = m + 1
			elif target < matrix[row][m]:
				r = m -1
			else:
				return True
		return False

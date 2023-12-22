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
	def searchMatrix(self,matrix,target):
		"""
		binsearch on cols first
		find row where l < t < r
		if value exists it'd have to be there
		pass that row into a binary search
		"""
		l = 0
		r = len(matrix) -1
		while l<=r:
			m = (l + r) //2
			if matrix[m][0] == target:
				return True
			# they're next to each other, pass in row to do binary search
			if r - l == 1:
				binsearch(matrix[m])
			if matrix[l][0] < target and matrix[m][0] > target:
				r = m 
				m = (l+r)//2
			elif matrix[m][0] < target and matrix[r][0] > target:
				l = m 
				m = (l+r)//2

			
		def binsearch(row):
			nonlocal target
			l = 0
			r = len(row) -1
			while l<=r:
				m = (l + r) //2
				if row[m] == target:
					return True
				# they're next to each other, pass in row to do binary search
				if row[l] < target and row[m] > target:
					r = m 
					m = (l+r)//2
				elif row[m] < target and row[r] > target:
					l = m 
					m = (l+r)//2
			return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
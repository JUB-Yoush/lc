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
			

def searchMatrix2(matrix,target):
	"""
	check when l<t<r
	it'd have to be in that row
	pass that row into a binary search
	"""
	pass

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
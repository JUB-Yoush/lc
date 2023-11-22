class Solution:
	def get_diameter(self,root):
			diameter = 0
			def dfs(root):   
				nonlocal diameter
				if root == None:
					return [0,-1]
				# get diameters of both children
				left = dfs(root.left)
				right = dfs(root.right)
				height = max(left[1],right[1]) + 1
				diameter = max(left[1] + right[1] + 2,diameter)
				return [left[1] + right[1] + 2,height]
			return dfs(root)[0]

class Solution2:
	def diameterOfBinaryTree(self,root):
		res = 0
		def dfs(root):
			if root == None:
				return -1
			left = dfs(root.left)
			right = dfs(root.right)
			res =max(res,2 + left + right)
			return 1+max(left,right)
	dfs(root)
	return res
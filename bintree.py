class TreeNode:
	def __init__(self, val=0, left=None,right=None):
		self.val = val
		self.right = right
		self.left = left

	def max_depth(self,root):
		if root == None: 
			return 0

		return 1 + max(self.max_depth(root.left),self.max_depth(root.right))

	def get_diameter(self,root):
		diameter = 0

		def dfs(root):   
			nonlocal diameter
			if root == None:
				return 0
			# get diameters of both children
			left = dfs(root.left)
			
	
	def is_balanced(root):
		pass

     


def make_tree(inputArr):
	# take an array of numbers and turn it into a binary tree
	# get index
	# value = value
	# childs are at 2i+1 and 2i+2

	node_arr = []
	for input in inputArr:
		node_arr.append(TreeNode(input))
		
	for i,node in enumerate(node_arr):
		child_l_pos = 2*i +1
		child_r_pos = 2*i +2
		if child_l_pos < len(node_arr):
			node.left = node_arr[child_l_pos]
		if child_r_pos < len(node_arr):
			node.right = node_arr[child_r_pos]
	return node_arr
	

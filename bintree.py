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
			right = dfs(root.right)
			diameter = max(left + right,diameter)
			return left + right
		return dfs(root)
	
	def is_balanced(root):
		"""
		dfs until at leaf
		return height and balance (base case is always balanced)
		check right and left children heights to calculate balance at current node
		return height and balance of self
		work your way back up
		"""
		def dfs(root):
			# return [height,is_balanced]

			if root == None:
				return [0,True]

			left_val = dfs(root.left)	
			right_val = dfs(root.right)
			is_balanced = left_val[1] and right_val[1] and abs(left_val[0] - right_val[0]) <= 1
			return [max(left_val[0],right_val[0]) + 1,is_balanced]

		return dfs(root)[1]

def render_tree(root):    
	# print it in the command line
	pass

def same_tree(root1,root2):
	# return if two trees are the same

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
		if node == None: continue
		if child_l_pos < len(node_arr) and node_arr[child_l_pos] != None:
			node.left = node_arr[child_l_pos]
		if child_r_pos < len(node_arr) and node_arr[child_r_pos] != None:
			node.right = node_arr[child_r_pos]
	return node_arr
	

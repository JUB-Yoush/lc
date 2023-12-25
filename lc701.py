# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
we don't need to maintain balance?
so just loop through the tree until where the values would be and add it there
'''
class Solution:
	def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		root_ref = root
		last_node = None
		if root == None:
			return TreeNode(val)
		while root != None:
			if root.val > val:
				if root.left == None:
					root.left = TreeNode(val)
					return root_ref
				root = root.left
			elif root.val < val:
				if root.right == None:
					root.right = TreeNode(val)
					return root_ref
				root = root.right


				
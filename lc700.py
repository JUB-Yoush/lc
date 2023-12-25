# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		while root != None:
			if root.val == val:
				return root
			if root.val > val:
				root = root.left
			if root.val < val:
				root = root.right
		return None
	
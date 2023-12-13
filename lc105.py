#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""
we need to use the facts from one table to inform the other table
put them together and they made the whole tree config
preorder = root, left, right
inorder = left, root, right
3 is certainly the root,
9 is certainly the left child of 3
when does it get ambiguous?
just considering preorder:
	- 9 could be on the right or left of 3
	- 20 could be a right child of 3 or a left child of 9
how does the inorder table help solve this?
	- as l,m,r 9 comes before 3, so 9 has to be a child of 3 and on the left

first pre value is always the root
this should be a hard bruh
preorder shows you which value is the root
inorder shows you the divide between the left side and right side
"""

class Solution:
	def buildTree(self, preorder, inorder):
		if not preorder or not inorder:
			return None
		def dfs(inorder,preorder):
			# first value of preorder is the root
			node = TreeNode(preorder[0],None,None)
			inorder_pos = inorder.index(preorder[0])
			preorder.pop(0)
			inorder.pop(inorder_pos)
			left_half = preorder[0:inorder_pos]
			right_half = preorder[inorder_pos:]
			node.left = dfs(inorder,left_half)
			node.right = dfs(inorder,right_half)
			return node
		return dfs(inorder,preorder)


import bintree
#https://leetcode.com/problems/flip-equivalent-binary-trees/
'''
just do a dfs but mirror the directions traveled?
and keep checking if the values are the same
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def flipEquiv(self, root1, root2) -> bool:
		def dfs(node1,node2):
			if node1 and node2 and node1.val == node2.val: 
				if node1.left == None and node1.right == None and node2.left == None and node2.right == None:
					return True
				else:
					if dfs(node1.left,node2.right) and dfs(node1.right,node2.left):
						return True
					else:
						return False
		return dfs(root1,root2)

tree1 = bintree.make_tree([1,2,3,4,5,6,None,None,None,7,8])[0]
tree2 = bintree.make_tree([1,3,2,None,6,4,5,None,None,None,None,8,7])[0]
print(Solution.flipEquiv(None,tree1,tree2))
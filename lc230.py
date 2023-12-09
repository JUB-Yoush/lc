import bintree
#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
just put all the nodes in a sorted array?
then return the ith index?
yeah that's it ig lol
"""

class Solution:
	def kthSmallest(self, root, k: int) -> int:
		nodes = []
		def dfs(root):
			nonlocal nodes
			if root != None:
				nodes.append(root.val)
				dfs(root.right)
				dfs(root.left)
		dfs(root)
		print(nodes)
		sorted_nodes = nodes.sort()
		return sorted_nodes[k]


tree = bintree.make_tree([5,3,6,2,4,None,None,1])
sol = Solution()
print(sol.kthSmallest(tree[0],3))
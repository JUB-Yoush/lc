class Solution:
	def goodNodes(self, root) -> int:
		"""
		could just check path from each node to root
		but that'll take a while
		keep track of root, and start at leaf
		move in once, and 
		somthing about if x is this number then all children can't be good
		keep track of higest value found
		all values lower aren't good
		"""
		good_nodes = 0
		def dfs(root,highest_val):
			nonlocal good_nodes
			if root != None:
				if root.val >= highest_val:
					good_nodes +=1
					highest_val = root.val
				dfs(root.right,highest_val)
				dfs(root.left,highest_val)
		dfs(root,root.val)
		return good_nodes

sol = Solution()
print(sol.goodNodes)
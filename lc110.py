import bintree
class Solution:
	def isBalanced(self,root):
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
			left_val = [0,True]
			right_val = [0,True]
			if root.left != None:
				left_val = dfs(root.left)	
			if root.right != None:
				right_val = dfs(root.right)
			is_balanced = abs(left_val[0] - right_val[0]) <= 1
			return [max(left_val[0],right_val[0]) + 1,is_balanced]
		return dfs(root)

tree = bintree.make_tree([1,2,2,3,3,None,None,4,4])[0]
sol = Solution()
print(sol.isBalanced(tree))
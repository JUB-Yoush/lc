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

			left_val = dfs(root.left)	
			right_val = dfs(root.right)
			is_balanced = left_val[1] and right_val[1] and abs(left_val[0] - right_val[0]) <= 1
			return [max(left_val[0],right_val[0]) + 1,is_balanced]

		return dfs(root)[1]


class Solution2:
	def isBalanced(self,root):
		def dfs(root):
			if root == None:
				return [True,0]
			
			left, right = dfs(root.left),dfs(root.right)
			balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1
			return [balanced, 1+max(left[1],right[1])]
		return dfs(root)[0]


tree = bintree.make_tree([1,2,2,3,None,None,3,4,None,None,4])[0]
sol = Solution()
print(sol.isBalanced(tree))
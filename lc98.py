import bintree
#https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
	"""
	leafs are binary search trees
	check if left and right are bst's
	check if you + kids are bst
	"""
	def isValidBST(self, root) -> bool:
		
		def dfs(root):
			if root == None: return True
			if root.left == None and root.right == None: return True

			bst_l = True
			bst_r = True

			if root.left != None and root.val <= root.left.val:
				bst_l = False
			
			if root.right != None and root.val >= root.right.val:
				bst_r = False

			is_bst = bst_r and bst_l

			kids_bst = dfs(root.left) and dfs(root.right)
			return is_bst and kids_bst
		return dfs(root)

tree = bintree.make_tree([2,1,3])
sol = Solution()
print(sol.isValidBST(tree[0]))


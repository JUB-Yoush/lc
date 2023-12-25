# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#https://leetcode.com/problems/path-sum/description/

'''
public variable path
recursive calls down each layer
if you reach a 0, then return false
'''

class Solution:
	def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
		def dfs(root,curr_sum):
			nonlocal targetSum
			if root == None:
				return curr_sum == targetSum
			curr_sum += root.val	
			dfs(root.right,curr_sum)
			dfs(root.left,curr_sum)


#neetcode
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        de = [
            (root, sum - root.val),
        ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False

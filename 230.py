# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        start from the rightmost value, list things from largest to smallest
        pop k-1 values, return 0
        """

        def dfs(node):
            if node == None:
                return
            global stack
            dfs(node.right)
            stack.append(node)
            dfs(node.left)

        stack = []
        curr = root
        dfs(curr)

        for i in range(k-1):
            stack.pop()

        return stack[-1]
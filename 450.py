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
        keep track of previous parent, when deleable node is found compare it's children to figure out which one would fit as it's replacement
        """

        curr = root
        prev = curr
        while True:
            if curr.val == key:




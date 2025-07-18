# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
every value can be inserted as a leaf?
I think?
binsearch to find spot, then insert?
"""


class Solution(object):
    def insertIntoBST(self, root, val):
        if root == []:
            return TreeNode(val)
        curr = root
        while True:
            if curr.val > val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return root
            if curr.val < val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return root

"""
find node to replace
find value to replace it with
overwrite value with new value
replace node of value taken
"""

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class wrongSolution:
    def deleteNode(self, root, key):
        def remove(node, parent):
            # if no kids, remove
            # if kids, swap appropriate value then remove kid
            if not node.left and not node.right:
                # remove (how)
            if node.right:
                node.val = node.right.val
                remove(node.right, node)
            if node.left:
                node.val = node.left.val
                remove(node.left, node)

        # search
        prev = root
        curr = root
        while curr:
            if curr == key:
                remove(curr, prev)
            if curr.val > key:
                prev = root
                curr = curr.left

            if curr.val < key:
                prev = root
                curr = curr.right

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            curr = root.right
            while curr.left:
                curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root


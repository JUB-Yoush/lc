#!/usr/bin/env python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        get the rightmost element of every level
        if we go from left to right in the queue then it'll be the last element of every level we search
        """

        queue = deque()
        output = []

        queue.append(root)

        while len(queue) != 0:
            output.append(queue[-1])
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return output

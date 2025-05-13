class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
add right child to the stack, by the time the left tree is done we've alredy dealt with the root
once we run into a null value, we know we can't go any further in the stack
add right to the stack, go to the left
once we hit null (can't go any more left), start poping the right values from the stack
curr is at some point left before being the middle, so it works out
"""


class Solution:
    def preorderTraversal(self, root) -> list[int]:
        stack = []
        res = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)  # could be null
                curr = curr.left
            else:
                curr = stack.pop()
        return res

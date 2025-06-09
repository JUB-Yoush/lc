# Definition for a binary tree node.
import bintree


"""
recursion
if left < curr and isValidBST(left)
we also need to maintain a previous max/min to make sure if dosent go above or below any previously found values
"""


class Solution:
    def isValidBST(self, root) -> bool:
        def helper(curr, left, right):
            if not curr:
                return True
            if not (left < curr.val < right):
                return False

            return helper(curr.left, left, curr.val) and helper(
                curr.right, curr.val, right
            )

        return helper(root, float("-inf"), float("inf"))


print(Solution.isValidBST(None, bintree.make_tree([5, 4, 6, None, None, 3, 7])[0]))

import bintree

# https://leetcode.com/problems/validate-binary-search-tree/
"""
recursive tree checking
recurse to leaf, leaf is bst
go up to parent, verify kids are bst + parent is in between kids in value
go left until no more left
go up one and check if left < curr
check if curr < right and right is bst
"""


class Solution:
    def isValidBST(self, root) -> bool:
        def dfs(curr):
            print(curr.val, curr.left, curr.right)
            leftgood = curr.left is None
            rightgood = curr.right is None
            if leftgood and rightgood:
                return True

            if curr.left is not None and curr.val > curr.left.val:
                leftgood = dfs(curr.left)

            if curr.right is not None and curr.val < curr.right.val:
                rightgood = dfs(curr.right)
            return leftgood and rightgood

        return dfs(root)


"""
dfs but pass in the... I wish python had type annotations. 
"""


class SolutionNeet:
    def isValidBST(self, root) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))


tree = bintree.make_tree([5, 1, 4, None, None, 3, 6])
sol = Solution()
print(sol.isValidBST(tree[0]))

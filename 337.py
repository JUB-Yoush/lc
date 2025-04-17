"""
house robber reivew: you want to pick the current + max of skipping next, or skip current and pick next
whichever gives you more money
in this version,  we can't rob 2 direcly linked nodes
so we either pick current + greatest of children of next node, or greatest from next node
it's not that different I think
"""


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # we don't know how many nodes there are.
        lvl_memos = []
        memo = {}

        def dfs(node):
            if node == None:
                return 0
            if node.left == None and node.right == None:
                memo[node] = node.val
                return

            memo[node] = max(
                node.val + max(get_child_max(node.left), get_child_max(node.right)),
                max(memo[node.left], memo[node.right]),
            )

        def get_child_max(node):
            # get's the grandchild value
            if node is None:
                return 0
            left_max = 0
            right_max = 0
            if node.left != None:
                left_max = memo[node.left]
            if node.right != None:
                right_max = memo[node.right]
            return max(left_max, right_max)

        # curr + max of children OR max of child

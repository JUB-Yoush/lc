# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swapChunk(self,root):
            # if it's not a leaf 
            if root and (root.right or root.left):
                #swap
                root.right,root.left = root.left,root.right
                swapChunk(self,root.right)
                swapChunk(self,root.left)

        swapChunk(self,root)

        return root
         
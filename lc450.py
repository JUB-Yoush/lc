# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
find the node
if node doesn't exist then do nothing
if node does exist then remove it
if right child then that's new parent
else left
if no kids then just leave it dude
'''
# fails case [5,3,6,2,4,null,7],5: expected:[6,3,7,2,4]
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root_ref = root
        parent = None
        while root != None:

            if root.val != key: #not at node yet
                if root.val > key:
                    parent = root
                    root = root.left
                elif root.val < key:
                    parent = root
                    root = root.right

            else: #found it
                if not root.left and not root.right: # if no kids
                    # was it a right kid or left kid of it's parent?
                    if parent == None:
                        return None
                    if parent.val > root.val: 
                        parent.left = None
                        return root_ref
                    elif parent.val < root.val:
                        parent.right = None
                        return root_ref

                if not root.left or not root.right: # if one kid swap kid value for the parents
                    if root.left == None:
                        root.val = root.right.val
                        root.right = None
                        return root_ref
                    elif root.right == None:
                        root.val = root.left.val
                        root.left = None
                        return root_ref

                #two kids
                # pick right to be new root and map the left to the right
                if root.left and root.right:
                    root.val = root.right.val
                    root.right = None
                    return root_ref
                    
                        
        return root_ref
                    


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor_p = None
        ancestor_q = None
        lca = root
        p_curr = root
        q_curr = root
        while True:
            if p_curr.val > p.val:
                #binary search
                ancestor_p = p_curr
                p_curr = p_curr.left
            elif p_curr.val < p.val:
                ancestor_p = p_curr
                p_curr = p_curr.right
            elif p_curr.val == p.val:
                ancestor_p = p_curr
            
            if q_curr.val > q.val:
                ancestor_q = q_curr
                q_curr = q_curr.left
            elif q_curr.val < q.val:
                ancestor_q = q_curr
                q_curr = q_curr.right
            elif q_curr.val == q.val:
                ancestor_q = q_curr

            if ancestor_p.val == ancestor_q.val:
                lca = ancestor_p
            else:
                return lca

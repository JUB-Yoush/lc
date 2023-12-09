class Solution:
	def isSubtree(self,root,subroot):
			if not subroot: return True
			if not root: return False
			if self.sameTree(root,subroot):
				return True

			return self.isSubtree(root.left) or self.isSubtree(root.right)
		
		def sameTree(p,q):
			if not p and not q:
				return True
			if p and q and p.val == q.val:
				return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
			else:
				return False
		
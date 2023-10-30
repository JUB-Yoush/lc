class Solution:
	def isSameTree(p,q):

		def sameSubTree(p,q):
			pLeaf = p.left == None and p.right == None
			qLeaf = q.left == None and q.right == None
			if pLeaf != qLeaf:
				return False
			elif pLeaf and qLeaf:
				return True
			
			if p.left == q.left and p.right == q.right:
				return sameSubTree(p.left,q.left)
			

class Solution:
	def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
		"""
		return the rightmost node of each list?
		"""
		res = []
		lowest_layer = -1
		def dfs(root,layer):	
			if root != None:
				if layer > lowest_layer:
					lowest_layer += 1
					res.append(root.val)
				dfs(root.right,layer +1)
				dfs(root.left,layer +1)
		dfs(root,0)
		return res
			
			

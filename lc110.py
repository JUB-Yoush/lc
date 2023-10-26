class Solution:
	def isBalanced(root):
		
		def dfs(root):
			if not root:return [True,0]
			left,right = dfs(root.left),dfs(root.right)
			bal = (left[0] and right[0]) and abs(left[1]-right[1])<= 1
			return [bal,1+max(left[1],right[1])] # return hight and balance
	
		return dfs(root)[0]
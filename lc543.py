def diameterOfBinaryTree(root):
	res = 0
	dfs(root)
	return res
def dfs(root):
	nonlocal res ##static function?

	if not root:
		return 0
	left = dfs(root.left)
	right = dfs(root.right)
	res = max(res, left+right)

	return 1 + max(left,right)

 
import binarytree
def maxDepth(root):
	print(root)
	return recursiveCheck(root)

def recursiveCheck(branch):
	print(branch)
	if branch.right != None:
		return 1 + recursiveCheck(branch.right)
	if branch.left != None:
		return 1 + recursiveCheck(branch.left)
	else:
		return 0

print(maxDepth(binarytree.tree(height=3)))
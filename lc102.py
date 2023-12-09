"""
 Notes:
 - recursion seems appropriate?
 - breadth first search
 - but maybe not recursion because the order of execution is all weird
 - you'd have to get left kid, right kid, and then go back to left kid to recurse.
 - have a queue for every node visited
	- add it's kids to the queue, then pop itself
 - how to tell when new layer?
 - how does the neetcode solution tell a new layer?
"""

class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		res = []
		q = collections.deque()
		q.append(root)
		while q:
			qLen = len(q)
			level = []
			for i in range(qLen): # per layer 
				node = q.popleft()
				if node:
					level.append(node.val)
					q.append(node.left)
					q.append(node.right)
			if level:
				res.append(level)
		return res
			
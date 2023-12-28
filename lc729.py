#https://leetcode.com/problems/my-calendar-i/
'''

'''
class TreeNode:
	def __init__(self, val=[0,0], left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class MyCalendar:

	def __init__(self):
		self.tree = []
		self.root = None


	def book(self, start: int, end: int) -> bool:
		curr_node = self.root
		if len(self.tree) == 0:
			root = TreeNode([start,end])
			
		while curr_node!= None:
			pass
		self.tree.append([start,end])
		return True
      
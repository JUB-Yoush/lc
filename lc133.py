#https://leetcode.com/problems/clone-graph/
'''
we start with one node and it's list of connections
make a copy of the node

make that node and then bfs into it's siblings?
but how do we know what the connections are on the other nodes?
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
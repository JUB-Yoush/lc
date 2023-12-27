#https://leetcode.com/problems/clone-graph/
'''
we start with one node and it's list of connections
make a copy of the node
 loop through it's neighbors
 make those nodes
 how do I ensure they're all connected?
 make a copy of first node
 map old node to new node
 go to first neighbour
 clone neigbhour
 go to it's first neighbor
 
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution1:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}
        def dfs(curr_node):
            new_node = Node(curr_node.val)
            oldtonew[curr_node] = new_node
            for neighbor in curr_node.neighbors:
                if neighbor not in oldtonew:
                    dfs(neighbor)
                new_node.neighbors.append(oldtonew[neighbor])
        dfs(node)
        return oldtonew[node] if node else None

#neetcode
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

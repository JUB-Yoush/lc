"""
hashmap of old nodes to new nodes
use to maintain connections
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        old2new = {}
        queue = []
        visited = set()
        if node.neighbors == []
            return Node(node.val)
        queue.append(node)

        while queue:
            curr = queue.pop()
            old2new[curr] = Node(curr.val)
            for nei in curr.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        for old, new in old2new.items():
            for nei in old.neighbors:
                new.neighbors.append(old2new[nei])

        return old2new[node]

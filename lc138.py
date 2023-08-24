"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes= []
        curr = head
        nodeHash = {}

        # make dc of each node, map to the hashmap
        while curr:
            newNode = Node(curr.val)
            nodeHash[curr] = newNode
            curr = curr.next
        nodeHash[None] = None 

        for oldNode,newNode in nodeHash.items():
            if oldNode != None:
                newNode.next = nodeHash[oldNode.next]
                newNode.random = nodeHash[oldNode.random]
        
        return nodeHash[head]
        

            

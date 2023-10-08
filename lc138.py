"""
import llist
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
        oldlist = head
        newlist = Node(head.val)
        newhead = newlist
        nodehash = {} #oldnode:newnode
        nodehash[oldlist] = newlist
        # populate hashmap
        while oldlist!= None:
            next = Node(oldlist.next.val)
            newlist.next = next
            newlist = next
            nodehash[oldlist] = newlist
            oldlist = oldlist.next
       
       # go again and assign rng ptrs 
        oldlist = head
        newlist = newhead
        while oldlist != None:
            newlist.random = nodehash[oldlist.random]
            newlist = newlist.next
            oldlist = oldlist.next
            
"""


def copyRandomList(head):
    oldToCopy = {None:None}
    curr = head
    while curr:
        copy = Node(cur.val)
        oldToCopy[curr]
        curr = curr.next
    curr = head
    while curr:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
    return oldToCopy[head]

    
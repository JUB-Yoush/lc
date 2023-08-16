import math
import llist

def middleNode(self, head):
    size = 0
    curr = head
    while curr != None:
        size += 1
        curr = curr.next
    curr = head
    target = int(size/2) 
    for i in range(target):
        curr = curr.next
    return curr
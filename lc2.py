# Definition for singly-linked list.
import llist
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

l1prev = None
l2prev = None
def addTwoNumbers(l1, l2):
    twohead = l2
    while l1 or l2 != None:

        if l1 == None: # if no next value add a leading 0
            l1 = ListNode(0)
            l1prev.next = l1
        if l2 == None: # if no next value add a leading 0
            l2 = ListNode(0)
            l2prev.next = l2

        sum = l1.val + l2.val
        if sum > 9: #if we need to move val up 
            if l1.next == None: # if no next value add a leading 0
                l1.next = ListNode(0)
            l1.next.val += 1 # add one (10)
            sum -= 10
        l2.val = sum
        
        l1prev = l1        
        l2prev = l2        
        l1 = l1.next
        l2 = l2.next
    return twohead


addTwoNumbers(llist.make_llist([9,9,9])[0],llist.make_llist([9,9,9])[0])


        
            


# Definition for singly-linked list.
import llist
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1, l2):
    twohead = l2
    while l1 and l2 != None:

        if l1 == None: # if no next value add a leading 0
            l1 = ListNode(0)
        if l2 == None: # if no next value add a leading 0
            l2 = ListNode(0)

        sum = l1.val + l2.val
        if sum > 9: #if we need to move val up 
            if l1.next == None: # if no next value add a leading 0
                l1.next = ListNode(0)
            l1.next += 1 # add one (10)
            sum -= 10
        l2.val = sum
        l1 = l1.next
        l2 = l2.next
    return twohead


addTwoNumbers(llist.make_llist([9,9,9])[0],llist.make_llist([9,9,9])[0])


        
            


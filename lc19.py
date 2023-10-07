
""" 
import llist
def removeNthFromEnd(head, n):
    # reverse list:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    revHead = prev
#    llist.print_list(revHead)
    curr = revHead
    if n == 1:
        curr = curr.next
    for i in range(n-1):
        prev = curr
        curr = curr.next
    prev.next = curr.next
#    llist.print_list(revHead)
    curr = prev
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
#    llist.print_list(prev)
    return prev
        

head = llist.make_llist([1,2,3,4,5])[0]
removeNthFromEnd(head,2)
"""
import llist
def removeNthFromEnd(head, n):
    dummy = llist.ListNode()
    dummy.next = head
    l = dummy
    r = dummy
    while r.next != None:
        if l.next != None:
            l = l.next 
        for i in range(n):
            if r.next != None:
                r = r.next
    l.next = l.next.next
    return dummy.next
    
head = llist.make_llist([1,2,3,4,5])[0]
removeNthFromEnd(head,2)
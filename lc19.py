import llist
def removeNthFromEnd(head,n): 
    curr = head
    delay = head
    while curr != None:
        for i in range(n):
            if curr != None:
                curr = curr.next
        if delay != None:
            delay = delay.next
    # node after delay is the one we need to rm
    if delay.next != 
    delay.next = delay.next.next
    return head 



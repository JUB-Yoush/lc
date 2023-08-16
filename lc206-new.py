import llist
def reverseList(head):
    prev = head
    curr = head.next
    if curr == None:
        return head
    
    while curr != None:
        after = curr.next
        curr.next = prev
        prev.next = None
        prev = curr
        curr = after
    return curr 


print(llist.print_list(llist.make_llist([0,1,2,3,4,5])[0]))



    


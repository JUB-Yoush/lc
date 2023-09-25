import llist
def mergeTwoLists(list1,list2):
    curr1 = list1
    curr2 = list2
    newlist = llist.ListNode()
    newlisthead = newlist
    '''
    compare current.val
    append lower one to dummy
    once one list runs out, append the rest of the other. 
    '''
    while curr1 != None and curr2 != None:
        if curr1.val <= curr2.val:
            newlist.next = curr1
            curr1 = curr1.next
        elif curr1.val >= curr2.val:
            newlist.next = curr2
            curr2 = curr2.next
        newlist = newlist.next
    
    if curr1 == None:
        newlist.next = curr2
    elif curr2 == None:
        newlist.next = curr1
    return newlisthead.next

print(llist.print_list(mergeTwoLists(llist.make_llist([1,2,4])[0],llist.make_llist([1,3,4])[0])))    
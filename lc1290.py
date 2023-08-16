import llist

def getDecimalValue(head) -> int:
    curr = head
    sum = 0
    n = -1
    
    while curr != None:
        curr = curr.next
        n += 1
    curr = head

    while curr != None:
        if curr.val == 1:
            sum += 2**n 
        n -= 1
        curr = curr.next
    return sum
head,tail = llist.make_llist([1,0,1,1,0,1,0])

print(getDecimalValue(head))

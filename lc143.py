import llist



"""
def reorderList(self,head):
    l = head
    r = head
    len = 1
    # r at end of list
    while r.next != None:
        len+= 1
        r = r.next
    moves = len//2 # number of nodes we'll have to swap

    for i in range(moves):
        temp = l.next
        l.next = r
        r.next = temp
"""


def reorderList(self,head):
    # find middle of list
    fast = head.next
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # flip 2nd half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    #merge halves
    first, second = head,prev
    while second:
        tmp1,tmp2 = first.next, second.next 
        first.next = second
        second.next = tmp1
        first,second = tmp1,tmp2

    
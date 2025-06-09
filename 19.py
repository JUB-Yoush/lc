"""
linked lists don't keep track of the previous value
we need to get nth from end
bf: count the number of nodes, then skip over that node on second pass
do it in one pass?
    Maintain two pointers and update one with a delay of n steps.
so when we reach the end of r, l will be at the value before the one we need to skip

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        lag = head
        curr = head
        delay = n
        if head.next is None:
            return None
        while curr.next is not None:
            # offset lag ptr by n
            if delay > 0:
                delay -= 1
            else:
                lag = lag.next
            curr = curr.next
        # lag is now at the value before the one to skip.
        # if value after skip, lag.next = lag.next.next, otherwise just remove final pointer

        # if lag didn't move, first value is to be removed
        if delay > 0:
            return head.next

        if lag.next.next is not None:
            lag.next = lag.next.next
        else:
            lag.next = None
        return head

"""
l1 and l2 at beginning
add number together, use dummy node to make new list
if number > 9, subtract by 9 and add it to the next value
if final number is >9, make a new node.
if l1 or l2 run out, just append the rest of the remaining one
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            sum = l1.val + l2.val
            # carry the 1
            if sum >= 10:
                sum -= 10
                if not l1.next:
                    l1.next = ListNode(0)
                if not l2.next:
                    l2.next = ListNode(0)
                l1.next.val += 1
            next_node = ListNode(sum)
            curr.next = next_node
            curr = next_node
            l1 = l1.next
            l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next

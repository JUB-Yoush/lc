"""
keep two pointers?
L and R
L.next = gcd(L,R)
gcd.next = R
move L up by 2
repeat?
seems to easy
it was that easy!
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def GCD(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


class Solution:
    def insertGreatestCommonDivisors(self, head):
        L, R = head, head.next
        while R is not None:
            gcd = ListNode(GCD(L.val, R.val), R)
            L.next = gcd
            L = R
            R = R.next
        return head

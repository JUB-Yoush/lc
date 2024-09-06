# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

#recursive
class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        newHead = head
        if head.next:
            self.reverseList(head.next)
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

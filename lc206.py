class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextNode= None
        curr = head
        prev = None

        while curr!= None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

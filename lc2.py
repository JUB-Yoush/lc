# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        sum = 0

        count = 0
        # get sum of values
        while curr1 or curr2:
            digit1 = 0
            digit2 = 0
            if curr1 != None:
                digit1 = curr1.val
                curr1 = curr1.next

            if curr2 != None:
                digit2 = curr2.val
                curr2 = curr2.next
            
            sum += (digit1 + digit2) * (10 ** count)
            count += 1

        dummy = ListNode()
        curr = dummy
        prev = dummy
        modSum = sum
        for digit in reversed(str(sum)):
            curr = ListNode(int(digit))
            prev.next = curr
            prev = curr
        
        return dummy.next

            
            

            


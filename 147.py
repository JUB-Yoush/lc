#https://leetcode.com/problems/insertion-sort-list/description/
"""
add values to list
sort list
turn list into llist
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        for i in range(1,len(values)):
            j=i
            while j > 0 and values[j] < values[j-1]:
                values[j], values[j-1] = values[j-1], values[j]
                j-=1

        curr = head
        while curr:
            curr.val = values.pop(0)
            curr = curr.next
        return head


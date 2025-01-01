#https://leetcode.com/problems/merge-k-sorted-lists/description/
"""
pass all the values into a list,
merge sort,
edit values and stitch llists to each other
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        values = []
        heads = []
        for list in lists:
            curr = list
            heads.append(list)
            while curr:
                values.append(curr.val)
                curr = curr.next

        values = values.sort()

        for i in range(len(lists)):
            curr = lists[i]
            while curr.next:
                curr.val = values.pop(0)
                curr = curr.next
            #stitch to other list head
            if lists[i+1] != None:
                curr.next = lists[i+1]
        return lists[0]





def mergeSort(values):
    length = len(values)
    if length == 0:
        return
    # base case: array is single item
    if length == 1:
        return values

    #split in half and recursively call
    mid = length // 2

    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    # take the two returned lists and stitch them back together
    return merge(left, right)

def merge(left, right):
    output = []
    i = j = 0

    # loop through each array and pick the lowest value at each point
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(left[j:])
    return output


#print(Solution.mergeKLists([[1,4,5],[1,3,4],[2,6]]))
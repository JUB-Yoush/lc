"""
just reverse the nodes in between left and rigth
how do we reverse a node in a linked list?
reverse section
have l -1 point to end of flip
have r + 1 point the beginning of flip
we could have two pointers that already exist at the offset of the values
so when R reaches it's value then L would be at it's value
actually idk man lets solve it without the stretch goal
"""


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        curr = head
        prel_value = None
        rvalue = None
        i = 0
        while curr is not None:
            if i == left-1:
                prel_value = curr
            elif i == right:
                rvalue = curr
            curr = curr.next
            i += 1
        curr = prel_value.next;
        prev =

        pass


'''
class Solution1:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

class Solution:
    def mergeTwoLists(self, list1, list2):
        curr1 = list1
        curr2 = list2
        newHead = ListNode()
        currNew = newHead
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                currNew.next = curr1
                currNew = currNew.next
                curr1 = curr1.next
            else:
                currNew.next = curr2
                currNew = currNew.next
                curr2 = curr2.next
        if curr1:
            currNew.next = curr1
        elif curr2:
            currNew.next = curr2
        return newHead.next
'''
class Solution:
    def countStudents(self, students, sandwiches):
        queue = students
        remaining = []
        prev_remaining = []

        while sandwiches:
            while queue:
                if queue[0] == sandwiches[0]:
                    queue.pop(0)
                    sandwiches.pop(0)
                else:
                    remaining.append(queue.pop(0))

            if remaining == prev_remaining:
                return len(remaining)

            queue = remaining
            prev_remaining = remaining.copy()
            remaining = []

        return 0

class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)


    def pop(self) -> int:
        for i in range(len(self.q) -1):
            self.q.push(self.popleft())
        return self.q.popleft()


    def top(self) -> int:
        return self.q[-1]


    def empty(self) -> bool:
        return len(self.q) == 0

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n < 0:
            return 0
        return self.climbStairs(n-1) + climbStairs(n-2)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head
        for i in range(index):
           curr = curr.next
           if curr == None:
            return -1
        if curr == None:
            return -1



    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val,self.head)
        self.head = newNode
        self.len += 1
        if self.len == 1:
            self.tail = self.head



    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val,None)
        self.tail.next = newNode
        self.tail = newNode
        self.len += 1
        if self.len == 1:
            self.tail = self.head


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.head
        for i in range(index):
           curr = curr.next
           if curr == None:
            return
        newNode = ListNode(val,curr)
        self.len += 1
        if self.len == 1:
            self.tail = self.head


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.head
        prev = curr
        for i in range(index):
            prev = curr
            curr = curr.next
            if curr == None:
                return
        prev.next = curr.next
        self.len -= 1
        if self.len == 1:
            self.tail = self.head



# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);
myLinkedList.get(1);
myLinkedList.deleteAtIndex(1);
myLinkedList.get(1);
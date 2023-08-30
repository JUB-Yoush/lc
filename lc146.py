class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



def reorderList(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    nodes = []
    dummy = ListNode()
    dummy.next = head
    curr = head
    foo = head

    while (foo):
        nodes.append(foo)
        foo = foo.next

    mid = len(nodes)//2
    firstHalf = nodes[:mid]
    secHalf = nodes[mid:]
    
    while (len(firstHalf)!= 0 or len(secHalf) != 0):
        curr.next = firstHalf[0]
        firstHalf.pop(0)
        curr = curr.next
        curr = secHalf[-1]
        secHalf.pop(-1)
        curr = curr.next
    
    if (len(firstHalf) != 0):
        curr.next = firstHalf[0]

    if (len(secHalf) != 0):
        curr.next = secHalf[0]
   
        

testcase = []
tc = ListNode(i+1)
prev = tc
for i in range(3):
    tc = ListNode(i+1,prev)
    testcase.append[tc]
    prev = tc

print(reorderList(testcase[0]))


class Node:
    def __init__(self,key,val):
        self.key, self.val = key,val
        self.prev = self.next = None


class LRUCache:
    def __init__(self,capacity:int):
        self.cap = capacity
        self.cache = {}
       #L = lru, right = most recent 
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next,nxt.prev = nxt,prev
    
    def insert(self,node):
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev


    def get(self, key: int) -> int:
        if key in self.cache:
            #todo: update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from ll and rm the LRU from the dictionary
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
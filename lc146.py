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


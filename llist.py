class ListNode:
    def __init__(self, val, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def make_llist(input)   : 
    head = ListNode(input[0])
    head.prev = None
    input.pop(0)
    prevNode = head
    for i,elem in enumerate(input):
        newNode = ListNode(elem)
        prevNode.next = newNode
        newNode.prev = prevNode
        prevNode = newNode
    tail = prevNode
    return head,tail

def print_list(head):
    output = ""
    curr = head 
    output += "["
    while curr.next != None:
        output += str(curr.val)
        curr = curr.next
        if curr.next != None:
            output += "->"
    output += "]"
    return output

    
        
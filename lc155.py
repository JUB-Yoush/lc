class MinStack:

    def __init__(self):
       self.stack = []
       self.minstack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0: self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# https://leetcode.com/problems/min-stack/
'''

'''
class MinStack:

    def __init__(self):
        # make stack obj with stack and min stack to maintain lowest

    def push(self, val: int) -> None:
        #append value to stack 

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
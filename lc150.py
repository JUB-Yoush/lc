#https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
add values to stack 
do operation on last two things
push result back onto the stack
'''
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            try:
                number = int(token)
                stack.append(number)
            except ValueError:
                if token =="+":
                    stack.append(stack.pop() + stack.pop())
                elif token =="-":
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second - first)
                elif token =="*":
                    stack.append(stack.pop() * stack.pop())
                elif token =="/":
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(second/ first))
        return stack.pop()

print(Solution.evalRPN(None,["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
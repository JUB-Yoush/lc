#https://leetcode.com/problems/baseball-game/
'''
easier polish notation question
append values to stack 
when operation: push value that is result of that operation
return sum of scores
'''
class Solution:
	def calPoints(operations):
		record = []
		for operation in operations: 
			if operation == '+': 
				record.append(record[-1] + record[-2])
			elif operation == 'D':
				record.append(record[-1] * 2)
			elif operation == 'C':
				record.pop()
			elif operation.isdigit() or operation[1:].isdigit():
				record.append(int(operation))
		return sum(record)

print(Solution.calPoints(["5","-2","4","C","D","9","+","+"]))
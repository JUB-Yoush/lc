#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
'''
0 = circle 1 = square
queue will be left with nothing but the same student and the opposite sandwich on top
repeat until that (how will we know?)
same student shows up twice and nobody else ate?
if sandwich == student then rm sandwich and student
if not then rm student and append to end, keep sandwich
'''
class Solution:
	def countStudents(students, sandwiches):
		didnt_eat_queue = []
		deq_len = 0
		while True:
			if len(students) ==0 and len(sandwiches) == 0: return 0
			if len(students) == 0:
				students = didnt_eat_queue
				didnt_eat_queue = []
				if len(students) == deq_len: #if no new students ate this cycle then we're stuck
					return len(students)
				deq_len = len(students)

			if students[0] == sandwiches[0]:
				del students[0]
				del sandwiches[0]
			else:
				didnt_eat_queue.append(students[0])
				del students[0]
			
				
print(Solution.countStudents([1,1,0,0],[0,1,0,1]))

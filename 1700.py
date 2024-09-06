#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
'''
instead of immedetly wrapping around, keep the students that didn't eat in a seperate list that we copy over
this way, we can check if the list we're going to copy over is the same as the existing list: meaning none of the kids ate
that way we know no more kids will eat.
'''

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        didnt_eat_queue = []
        prev_eat_queue = []

        while True:
            while len(students) > 0:
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    didnt_eat_queue.append(students[0])
                    students.pop(0)
            if len(didnt_eat_queue) > 0:
                if didnt_eat_queue == prev_eat_queue: #nobody new ate, nobody else can eat
                    return len(didnt_eat_queue)
                else:
                    prev_eat_queue = didnt_eat_queue.copy()
                    students = didnt_eat_queue.copy()
                    didnt_eat_queue = []
            else:
                return 0

print(Solution.countStudents(None,[1,1,0,0],[0,1,0,1]))







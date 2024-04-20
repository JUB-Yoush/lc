# https://leetcode.com/problems/course-schedule-ii/description/
'''
dude I should be able to solve this
make adj list
loop from course with no pre reqs
if reached class with no neighbors, start to return inputs
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        adj_list = [] * numCourses
        for prereq in prerequisites:
            adj_list[prereq[1]].append(prereq[0])

        def dfs(visited,curr_course,prev_course):
            if curr_course in visited:
                return []
            set.append(curr_course)
            for course in 
            pass


        for i in range(numCourses):
            if adj_list[i] == []:
                dfs(set(),i,None)
                break
        


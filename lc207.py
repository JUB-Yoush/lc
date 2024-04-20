#https://leetcode.com/problems/course-schedule/description/
'''
classical adjacency list problem.
bf:
- find the courses with no pre-reqs and take those first
- see what's available afterwards
- repeat that until all the courses have been taken?

make a hashmap of a course and it's prereqs
do a dfs starting at whatever I guess
when we return from a value pop it from the list of prereqs
'''



'''
back at it again
create a hashmap of a course and it's prereqs
traverse though the array in a bfs and check if all courses have all their pre-reqs gone?
[[0,1],[0,2],[1,3],[1,4],[3,4]]
hashmap:
0:1,2
1:3,4
3:4
4:None
pick first course and traverse though, see if you can reach everything else?
start at 0
go to 1 
goes to 3
goes to 4
nowhere to go, unmark 4 from 3
unmark 3 from 1
unmark 1 from 0
go to 2
unmark 2 from 0 
0 has no pre-reqs
move to next course
(when you reach a course from a certain course, remove that prereq from that courses hashmap key???)
'''
class Soluti:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # stores course as key and prereqs as values
        courseMap = {}

        def dfs(parentCourse,currCourse):
            for preReq in courseMap[currCourse]:
                dfs(currCourse,preReq)
            if len(courseMap[currCourse]) == 0:
                courseMap[parentCourse].remove(currCourse)
                return
                
        for course in prerequisites:
            if course[0] not in courseMap:
                courseMap[course[0]] = []
            courseMap[course[0]].append(course[1])
       
            for i in range(numCourses):
                #if it has pre-reqs
                if i in courseMap:
                    if len(courseMap[i]) != 0:
                        pass

            
            for i in range(numCourses):
                if i in courseMap:
                    if courseMap[i] != []:
                        return False
            return True



'''
had to (keep) doing it to em
instead of a hashmap, I could use an array
I could dfs over every prereq in the array
then finally loop back over it and check that all prereqs are empty
if not empty then return false
'''


class Solutio:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        visited = set()
        courses = [[]] * numCourses
        for preReq in prerequisites:
            courses[preReq[0]].append(preReq[1])

        def dfs(prevCourse,currCourse):
            
            if currCourse in visited:
                return False
            if courses[currCourse] == []:
                return True
            
            visited.add(currCourse)
            for i in range(len(courses[currCourse])):
               if not dfs(i,courses[i][0]): return False
            visited.remove(currCourse)
            courses[currCourse] = []
            return True

        for i in range(len(courses)):
            if len(courses[i]) != 0:
                dfs(i,courses[i][0])
        





'''
create graph based on pairs
graph is directed, prereqes aren't commutitive
start from course w no pres, traverse from one course to another in a dfs, maintain visited set
if you were able to add every course to your visited set then it's true
remove prereqs as you find them
if not then you could never reach every course, so it's false?
'''
class Solution:
    def canFinish(self, numCourses, prerequisites):

        course_graph = [[] for _ in range(numCourses)]
        
        for course in prerequisites:
            course_graph[course[0]].append(course[1])

        def dfs(i):
            for prereq in course_graph[i]:
                if len(course_graph[prereq]) == 0 or course_graph[prereq][0] == -1:
                    course_graph[i].remove(prereq)
                if dfs(prereq): 
                    course_graph[i].remove(prereq)
            course_graph[i].append(-1)
            return True
        
        dfs(0)
        for course in course_graph:
            if course != []:
                return False
    
print(Solution.canFinish(None,5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))
        
        

        
        





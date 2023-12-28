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
#neetcode, will review question
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


'''
back at it again
create a hashmap of a course and it's prereqs
traverse though the array in a bfs and check if all courses have all their pre-reqs gone?
(when you reach a course from a certain course, remove that prereq from that courses hashmap key???)
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
# https://leetcode.com/problems/course-schedule/description/
"""
form adj list
check if one has no prereqs
traverse list starting from course with no prereqs
check for cycle in directed graph
if we're ever sent back to a node we've visited, that's a cycle
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        if numCourses == 1:
            return True

        def dfs(course: int, path: set) -> set:
            # if cycle, can't take anything we've found
            if course in path:
                return set()
            path.add(course)

            # at course with no courses to go to
            if prereq_to_course[course] == []:
                course_to_prereq[course] = []
                return path

            for nei in prereq_to_course[course]:
                return dfs(nei, path)

            # appease pyright
            return set()

        course_to_prereq = {i: [] for i in range(numCourses)}
        prereq_to_course = {i: [] for i in range(numCourses)}
        taken_courses = set(range(numCourses))

        # make graph
        for course, prereq in prerequisites:
            course_to_prereq[course].append(prereq)
            prereq_to_course[prereq].append(course)

        # traverse graph
        for i in range(numCourses):
            if course_to_prereq[i] == [] or i not in taken_courses:
                visited = set()
                visited.add(i)

                for j in prereq_to_course[i]:
                    able_to_take = dfs(j, visited)
                    taken_courses -= able_to_take
                    if len(taken_courses) == 0:
                        return True
        return False


print(Solution.canFinish(None, 5, [[1, 4], [2, 4], [3, 1], [3, 2]]))

# print(Solution.canFinish(None, 2, [[1, 0]]))

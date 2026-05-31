class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses[course].append(prereq)

        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if courses[course] == []:
                return True
            visiting.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            courses[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
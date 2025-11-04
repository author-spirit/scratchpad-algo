"""
Ref: https://leetcode.com/problems/course-schedule/description/
"""

def can_finish(numCourses: int, prerequisites):
    adjList = {n: [] for n in range(numCourses)}
    for cur, pre in prerequisites:
        adjList[cur].append(pre)

    visited = [None]*numCourses
    def is_cyclic(n):
        if visited[n] == 1:
            return True

        if visited[n] == 2:
            return False

        visited[n] = 1
        for i in adjList[n]:
            if is_cyclic(i):
                return True

        visited[n] = 2
        return False


    for n in range(numCourses):
        if is_cyclic(n):
            return False

    return True

prereq = [[0,1], [0,2], [1,3], [1,4], [3,4]]
# prereq=[[1,0],[0,1]]
n=5

print("Can finish the course? ", can_finish(n,prereq))

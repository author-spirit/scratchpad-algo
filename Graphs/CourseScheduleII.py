"""
Ref: https://leetcode.com/problems/course-schedule-ii/
"""

prerequisites = [[0,1], [0,2], [1,3], [1,4], [3,4]]
#prerequisites = [[1,0],[2,0],[3,1],[3,2]]
prerequisites = [[2,3],[1,2],[0,1],[0,4],[4,5],[5,1]]
numCourses = 6
ROWS = len(prerequisites)
COLS = len(prerequisites[0]) if ROWS else 0

adjList = {p: [] for p in range(numCourses)}
for cur, pre in prerequisites:
    adjList[cur].append(pre)

# 1: Visiting, 2:Visited
visited = [None] * numCourses
stack = []

def dfs(node):
    if visited[node] == 1:
        print("Still visiting (cyclic)", node)
        return False

    if visited[node] == 2:
#        print("Already visited", node)
        return True
    
    visited[node] = 1
    for n in adjList[node]:
        if not dfs(n):
            return False

    visited[node] = 2
    stack.append(node)
    return True

for i in range(numCourses):
    if not dfs(i):
        break
print("Visited", visited)
print("Stack", stack)

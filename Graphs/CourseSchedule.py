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


def kahns(numCourses: int, prerequisites):
    adj_list = {k: [] for k in range(numCourses)}

    for cur, pre in prerequisites:
        adj_list[cur].append(pre)

    stack = []
    indegree = [0 for _ in range(numCourses)]

    # calculate indeg
    for u in range(numCourses):
        for v in adj_list[u]:
            indegree[v] +=1

    from collections import deque
    que = deque()

    # add zero in-degrees to queue
    for idx,val in enumerate(indegree):
        if val == 0:
            que.append(idx)

    while que:
        node = que.popleft()
        for nei in adj_list[node]:
            indegree[nei] -=1
            if indegree[nei] == 0:
                que.append(nei)
        
        stack.append(node)

    print(stack)
    return len(stack) == numCourses

prereq = [[0,1], [0,2], [1,3], [1,4], [3,4]]
prereq=[[1,0],[0,1]]
n=5

# Naive DFS approach
print("Can finish the course? ", can_finish(n,prereq))

# Using Topological Sorting (Kahn's)
print("Can Finish?",kahns(n,prereq)) 

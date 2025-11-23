"""
Topological Sort is linear ordering of vertices such that
exist edge between u & v where u appears before v.

(5)---->(0)<-----(4)
 |                |
 |                |
 |                |
 ⌄                ⌄
(2)---->(3)----->(1)

"""

graph = [[],[],[3],[1],[0,1],[0,2]]
v=6

toposort = []    # stack
indeg = [0 for _ in range(v)]

# 1. calculate in-degree
for neis in graph:
    for nei in neis:
        indeg[nei] +=1

from collections import deque
que = deque()

# 2. add zero in-degrees to queue

for idx, deg in enumerate(indeg):
    if deg == 0:
        que.append(idx)

while que:
    node = que.popleft()
    
    # run and decrease the current node neighbour's in-degree
    for nei in graph[node]:
        indeg[nei] -=1
        if indeg[nei] == 0:
            que.append(nei)

    toposort.append(node)
    
print("Toposort", toposort if len(toposort) ==v else 'cycle detected')

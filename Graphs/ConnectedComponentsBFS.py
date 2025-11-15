"""
Ref: https://takeuforward.org/plus/dsa/problems/connected-components
"""

edges = [[0, 1], [1, 2], [3, 4]]
v = 5

# Get the undirected adjacency list
adjlist = {k: [] for k in range(v)}

for cur, prev in edges:
    adjlist[cur].append(prev)
    adjlist[prev].append(cur)

print("AdjList: ", adjlist)

from collections import deque

que = deque()

def bfs(node):
    visited.add(node)
    que.append(node)
    
    while que:
        vertex = que.popleft()
        print(vertex)
        for nei in adjlist[vertex]:
            if nei in visited:
                continue

            que.append(nei)
            visited.add(nei)

visited = set()
count = 0
for i in range(v):
    if i in visited:
        continue

    bfs(i)
    count +=1

print("# of components", count)

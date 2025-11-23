"""
Directed Acyclic Graph (DAG), the nodes are connected with 
directed edges where there exist no cycle.

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
visited = set()

def dfs(node):
    if node in visited:
        return
    
    visited.add(node)
    for nei in graph[node]:
        dfs(nei)
    
    toposort.append(node)

for i in range(v):
    dfs(i)

print("Toposort", toposort)

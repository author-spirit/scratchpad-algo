"""
Ref: https://takeuforward.org/data-structure/shortest-path-in-directed-acyclic-graph-topological-sort-g-27

## Shortest Path in DAG
Based on Topological Sort

## Steps:
- Prepare Adjacency list in pairs
- Get results in stack using "Topological Sort"
- Unstack and calculate the distance
"""

edges = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
m=7
n=6
source = 0

edges = [[0,4,2], [0,5,3], [5,4,1], [4,6,3], [4,2,1], [6,1,2], [2,3,3], [1,3,1]]
m=8
n=7

# 1. prepare adjacency list on pairs
adj_list = {k: [] for k in range(n)}

for u,v,wt in edges:
    adj_list[u].append((v,wt))

# 2. Perform Toposort and keep track in stack
visited = set()
stack = []
def toposort(n):
    if n in visited:
        return

    visited.add(n)
    for nei in adj_list[n]:
        toposort(nei[0])
    stack.append(n)

for i in range(n):
    toposort(i)

# 3. Unstack the elements and calculate distance with initial infinity
dis = [float('inf') for i in range(n)]
# assuming source is zero'th
dis[0] = 0

while stack:
    node = stack.pop()
    for nei in adj_list[node]:
        # current_node_distance + neighbour weight < neighbour distance
        if dis[node] + nei[1] < dis[nei[0]]:
            dis[nei[0]] = dis[node] + nei[1]

for idx, st in enumerate(dis):
    if st == float('inf'):
        dis[idx] = -1

print(dis)

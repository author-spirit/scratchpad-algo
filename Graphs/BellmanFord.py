"""
Bellman Ford Algorithm
"""

edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
edges = [ [0, 1, 1], [1, 2, -1], [2, 0, -1] ]
n=3

dis = [float('inf')] * n

src = 0
dis[src] = 0

# iterate n-1 and relax the edges
for i in range(n):
    for u,v,w in edges:
        # guard against unreachable node from source
        if dis[u] != float('inf') and dis[u] + w < dis[v]:
            dis[v] = dis[u] + w

# If possible to do relaxation on Nth iteration
# then negative cycle exists
for u,v,w in edges:
    if dis[u] != float('inf') and  dis[u] + w < dis[v]:
        print("Negative Cycle")
        break

print(dis)


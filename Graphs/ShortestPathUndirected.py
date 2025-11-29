"""
Ref: https://takeuforward.org/data-structure/shortest-path-in-undirected-graph-with-unit-distance-g-28/

Shortest Path in Undirected Graph
---
Reach from source to destination in shortest path, 
the default distance will be 1.
The best traversal method is BFS, it ensure that it visits 
all the nodes in level-wise, and adds to queue.

Steps:
- Move the graph to adjacency list
- Create "distance array" to track the distances, initially set to infinity
- Set the source node's distance 0, add immediately to  to queue
- pop the element from queue, scan the current node's neighbours
- calculate the distance - 1 + current_distance < neighbour distance, 
    if new distance is lesser than neighbour then update the neigh's distance
    add add them to queue, otherwise ignore. (Infinity/MAX_INT distances are unvisited)
- repeat 3,4 until the queue gets empty
- Move all distances to "result array", change the infinity distance to -1
"""

edges = [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6],[1, 2], [2, 6], [6, 7], [7, 8], [6, 8]]
source = 0

m = 9

adj_list = {i: [] for i in range(m)}

# Undirected Adjacency list
for u,v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

print(adj_list)

# Initial distance, queue
distance =[float('inf') for _ in range(m)]
distance[source] = 0

from collections import deque
que = deque([source])

# scan, update distance
# default distance = 1
while que:
    node = que.popleft()
    for nei in adj_list[node]:
        cur_dis = 1 + distance[node]
        nei_dis = distance[nei]
        if cur_dis < nei_dis:
            distance[nei] = cur_dis
            que.append(nei)    # TODO, can already visited node is added to queue?

for idx,dis in enumerate(distance):
    if dis == float('inf'):
        distance[idx] = -1

print(distance)




"""
Prim Algorithm:
    Compute and reduce the graph to MST

Requirements:
    Visited Array, Priority Queue (MinHeap), MST Result & Sum

Add the node to priority queue with weight (weight, node, parent)
deque check if visited then skip else make it visited, add to mst and increment the sum
scan all the adjacent nodes add them to MinHeap.
Repeat until there is no nodes left and PQ is empty.
"""

import heapq

# v, w, undirected
adj_list = [
    [(1,2), (2,1)],
    [(0,2), (2,1)],
    [(0,1), (1,1), (4,2), (3,2)],
    [(2,2), (4,1)],
    [(2,2), (3,1)]
]

n = 5

visited = [0 for _ in range(n)]

# weight, node, parent
heap = [(0,0,-1)] # initial config
mst = []
sum = 0

while heap:
    node_wt, node, parent = heapq.heappop(heap)
    if visited[node] == 1:
        continue

    visited[node] = 1

    if parent != -1:
        mst.append((parent, node))

    sum += node_wt

    # scan adjacent list
    for nei in adj_list[node]:
        v,nei_w = nei
        if visited[v] ==1:
            continue

        heapq.heappush(heap, (nei_w, v, node))

print("MST Sum", sum)
print("MST Graph", mst)

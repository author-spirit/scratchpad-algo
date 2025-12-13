"""
# Dijsktra's Algorithm
## Shortest Path in weighted graph

Ref: https://takeuforward.org/data-structure/dijkstras-algorithm-using-set-g-33
"""

import heapq

heap = []

adj = {
    0: [(1, 2), (2, 4)],
    1: [(0, 2), (2, 1), (3, 7)],
    2: [(0, 4), (1, 1), (3, 3)],
    3: [(1, 7), (2, 3), (4, 1)],
    4: [(3, 1)]
}

# graph in my notebook
adj = {
  0: [(1,4), (2,8)],
  1: [(0,4), (4,6)],
  2: [(0,8), (3,2)],
  3: [(2,2), (4,10)],
  4: [(1,6), (3,10)]
}

m = 5

adj = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 7)],
    2: [(0, 4), (1, 2), (3, 1), (4, 5)],
    3: [(1, 7), (2, 1), (4, 3)],
    4: [(3, 3), (2, 5)]
}

adj = {
    0: [(1, 5), (2, 2)],
    1: [(3, 6), (4, 20)],
    2: [(1, 1), (3, 4)],
    3: [(4, 2)],
    4: []
}

distance = [float('inf') for _ in range(m)]

# source=0, set distance[0] to 0 and add to PQ
distance[0] = 0
heapq.heappush(heap, (0,0))

# scan until heap list gets empty
while heap:
    # pop the smallest weighted element/node
    cur_dis, cur_node = heapq.heappop(heap)

    # NOTE: check if entry is outdated and overtaken by better distance
    if cur_dis != distance[cur_node]:
        print(f"Node '{cur_node}' is outdated ({cur_dis})")
        continue

    # new distance = min(nei_dis, cur_node_dis + nei_weight)
    # scan all neighbours, calculate distance and add to PriQ
    for v,wt in adj[cur_node]:
        new_distance = cur_dis + wt        
        if new_distance < distance[v]:
            heapq.heappush(heap, (new_distance, v))
            distance[v] = new_distance

print("Shortest Path (dis): ",distance) 

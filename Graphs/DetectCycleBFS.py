"""
Ref: https://takeuforward.org/data-structure/detect-cycle-in-an-undirected-graph-using-bfs/

Detect Cycle in an Undirected Graph (using BFS)

"""

v=5
edges = [[1,2],[1,3],[3,4],[3,5],[4,5]]

adj_list = {k: [] for k in range(1,v+1)}

for cur, prev in edges:
    adj_list[cur].append(prev)
    adj_list[prev].append(cur)

print(adj_list)


visited = set()
from collections import deque


def is_cycle():
    que = deque()
    que.append((1,0))

    while que:
        node,prev = que.popleft()
        for nei in adj_list[node]:
            if nei == prev:
                continue

            if nei in visited:
                return True

            que.append((nei,node))
            visited.add(node)

    return False


print("Is Cycle: ", is_cycle())

"""
Name: Bipartite Graph
Ref: https://leetcode.com/problems/is-graph-bipartite/description/
Date: Nov 22, 2025

Pattern: Graph Coloring using BFS to detect odd cycles
"""

# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]     # False
graph = [[1,3],[0,2],[1,3],[0,2]]           # True
# graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]        # False

odd = [0 for _ in range(len(graph))]        # 1: Odd; -1: Even

# BFS
from collections import deque

def is_bipartite():
    que = deque()
    for i in range(len(graph)):
        if odd[i] != 0:
            continue

        que.append(i)
        odd[i] = -1         # even, can be odd

        while que:
            node = que.popleft()
            for nei in graph[node]:
                print((node, nei))
                if odd[nei] == 0:
                    odd[nei] = -1 if odd[node] == 1 else 1
                    que.append(nei)
                elif odd[nei] == (odd[node]):
                    # if the current node and its neighbour are same color stop it.
                    return False

    return True

print(is_bipartite())
print(odd)

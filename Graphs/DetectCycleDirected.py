"""
Detect Cyclic using Kahn's Algorithm
"""

V = 4

# Adjacency list representing directed graph
adj = [
    [1], [2], [3], [1]  
]

indeg = [0 for _ in range(V)]
for u in range(V):
    for v in adj[u]:
        indeg[v] +=1

count = 0
from collections import deque
que = deque()

for idx, d in enumerate(indeg):
    if d == 0:
         que.append(idx)

while que:
    node = que.popleft()
    for nei in adj[node]:
        indeg[nei] -=1
        if indeg[nei] == 0:
            que.append(nei)

    count +=1

print("Cycle exists" if V != count else "Yay! No Cycle exists")

"""
Ref:https://neetcode.io/solutions/number-of-connected-components-in-an-undirected-graph
"""

n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

adjList = {k: [] for k in range(n)}

for cur,nxt in edges:
    adjList[cur].append(nxt)
    adjList[nxt].append(cur)

print(adjList)
import sys

visited = [None] * n
stack = []

def dfs(node):
    if visited[node]:
        return 
    
    visited[node]=1
    for i in adjList[node]:
        print((node,i))
        if not visited[i]:
            dfs(i)
        else:print(f"{i} already visted")

count = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        count+=1
    else:print(f"{i} already visted")

print("Connected Count:", count)

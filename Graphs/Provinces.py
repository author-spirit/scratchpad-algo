"""
Ref: https://leetcode.com/problems/number-of-provinces/
"""

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]

def dfs(node):
    if node in visited:
        return

    visited.add(node)
    for i in range(len(isConnected[node])):
        if isConnected[node][i] and i not in visited:
            dfs(i)

# scan through all rows * columns
# If node marked with 1 then enter in..
rows = len(isConnected)
cols = len(isConnected[0])
visited = set()
count = 0
for i in range(rows):
    for j in range(cols):
        if isConnected[i][j] and j not in visited:
            dfs(j)
            count+=1

print("Count", count)


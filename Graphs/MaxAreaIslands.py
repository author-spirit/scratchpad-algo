"""
Ref: https://leetcode.com/problems/max-area-of-island/description/
"""

nodes = [[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]
nodes = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
nodes = [[0,0,0,0,0,0,0,0]]

visited = set()
rows = len(nodes)
columns = len(nodes[0])
maxi = {}

DIRECTIONS = ((0,-1), (-1,0), (0,1), (1,0)) # 4 Direction

def dfs(node, sign):
    if node in visited:
        return

    if (node[0] < 0 or node[1] < 0) or (node[0] >= rows or  node[1] >= columns):
        return
    
    print(node)
    visited.add(node)
    maxi[sign] = maxi.get(sign,0) + 1
    for direction in DIRECTIONS:
        row = node[0] + direction[0]
        col = node[1] + direction[1]

        if row >= 0 and col >= 0 and row < rows and col < columns and nodes[row][col]:
            print(node, (row, col), sign)
            dfs((row,col), sign)

sign = 0
# Traversing Each node by rows-columns
# If any of the node/vertex is 1 and row-column not in visited set then perform DFS, otherwise skip
for i in range(rows):
    for j in range(columns):
        if nodes[i][j] == 1 and (i,j) not in visited:
            dfs((i,j),sign)
            sign += 1

print(maxi)
print(max(maxi.values()) if maxi else 0)

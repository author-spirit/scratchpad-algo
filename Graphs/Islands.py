"""
Ref: https://leetcode.com/problems/number-of-islands/
"""

nodes = [[1,1,0], [1,1,0], [0,0,1]]
nodes = [[1,0,0], [0,1,0], [0,0,1]]
nodes = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]

count = 0
visited = set()
rows = len(nodes)
columns = len(nodes[0])

direction = ((0,-1), (-1,0), (0,1), (1,0))

def dfs(i,j):
    if (i < 0 or i >= rows) or (j < 0 or j >= columns):
        return

    for probe in direction:
        row = i + probe[0]
        col = j + probe[1]
        if (row,col) in visited or row >= rows or col >= columns:
            continue

        visited.add((row,col))
        if nodes[row][col] == 1:
            dfs(row,col)


for i in range(rows):
    for j in range(columns):
        if nodes[i][j] == 1 and (i,j) not in visited:
            count += 1
            dfs(i,j)

print("Final Count", count)

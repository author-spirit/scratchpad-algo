"""
Shortest Path in Binary Matrix

Ref: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
Patterns: bfs, matrix
"""

from collections import deque

def bfs_matrix(grid):
    visited = set()

    N = len(grid)
    que = deque()
    que.append((1, 0, 0))    # source, row, col
    directions = ((0,1), (1,0), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1))

    while que:
        dis, row, col = que.popleft()
        if (row, col) in visited or grid[row][col] == 1:
            continue

        if (row, col) == (N-1, N-1):
            return dis

        visited.add((row, col))

        print("dis", dis, (row, col))

        for direct in directions:
            nrow = row + direct[0]
            ncol = col + direct[1]

            if 0 <= nrow < N and 0 <= ncol < N and \
                grid[nrow][ncol] == 0 and \
                (nrow, ncol) not in visited:
                que.append((dis + 1, nrow, ncol))

    return -1

res = bfs_matrix([[0,0,0],[1,1,0],[1,1,0]])
print(res)

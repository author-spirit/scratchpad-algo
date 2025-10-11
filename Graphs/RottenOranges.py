"""
Ref: https://leetcode.com/problems/rotting-oranges/description/
"""
from collections import deque

grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
#grid = [[0,2]]

rows = len(grid)
cols = len(grid[0])
queue = deque()
direction = ((-1,0), (0,-1), (1,0), (0,1))
fresh = 0

# Step 1: Get the fresh count, initiate queue
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            fresh+=1
        elif grid[i][j] == 2:
            queue.append((i,j))

# Step 2: Start queue, scan on 4 direction then rot it, keep track of rotten count
minute = 0
while queue and fresh > 0:

    # multi-source BFS, meaning run the BFS simultaneously on multiple nodes
    # First, group of 4 direction nodes are iterated, then proceeds to next set of 4 direction nodes (within 4)
    minute +=1
    for i in range(len(queue)):

        # scan in 4 direction
        dq=queue.popleft()
        for path in direction:
            row = dq[0] + path[0]
            col = dq[1] + path[1]

            # make fresh ones rotten and add them to queue
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = 2
                fresh -=1
                queue.append((row,col))

unit = minute if fresh == 0 else -1
print("Total minutes:", unit)

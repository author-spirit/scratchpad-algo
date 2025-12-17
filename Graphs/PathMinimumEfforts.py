"""
1631. Path With Minimum Effort

Ref: https://leetcode.com/problems/path-with-minimum-effort/description/

Patterns: bfs, dijkstra
Intuition: Choose minimum difference between adjacent nodes
"""
import heapq

visited = set()
directions = ((0,1), (1,0), (0,-1), (-1,0))   # just 4 direction
heights = [[1,2,2],[3,8,2],[5,3,5]]
ROWS = len(heights)
COLS = len(heights[0])

# source initialization
# heap 
heap = [(0,0,0)]

while heap:
    diff, row, col = heapq.heappop(heap)
    
    # skip to avoid outdated entries
    if (row, col) in visited:
        continue

    if row == ROWS - 1 and col == COLS - 1:
        print("Minimum effort", diff)
        break
    
    visited.add((row,col))
    # adjacency nodes - 4 Directions
    for direct in directions:
        nrow = row + direct[0]
        ncol = col + direct[1]

        print("old", (row, col), "new", (nrow, ncol))

        # within range
        if 0 <= nrow < ROWS and 0 <= ncol < COLS and (nrow, ncol) not in visited:
            diff = abs(heights[nrow][ncol] - heights[row][col])
            heapq.heappush(heap, (diff, nrow, ncol))

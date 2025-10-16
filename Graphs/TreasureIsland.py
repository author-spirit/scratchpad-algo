"""
Ref:https://leetcode.com/discuss/post/347457/amazon-oa-2019-treasure-island-by-sithis-yaz2/ 
"""

grid = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]

# BFS, multi-source with tracker

from collections import deque

queue = deque()
queue.append([0,0])

ROW = len(grid)
COL = len(grid[0])

directions = ((0,-1), (-1,0), (0,1), (1,0))

def scan():
    tracker = 0
    while queue:
        # tracker is increment only on complete dequeue of group
        # tracker will be accurate until X is found
        
        tracker +=1
        print(queue)
        for q in range(len(queue)):
            node = queue.popleft()

            for path in directions:
                row = node[0] + path[0]
                col = node[1] + path[1]
                
                print((row,col))
                # scan in all four directions
                # queue the '0', and mark that place danger so next node will not visit
                if 0 <= row < ROW and 0 <= col < COL:
                    if grid[row][col] == 'O':
                        queue.append((row,col))
                        grid[row][col] = 'D'
                
                    if grid[row][col] == 'X':
                        return tracker

    return tracker

count = scan()
print("Shortest path to reach island", count)

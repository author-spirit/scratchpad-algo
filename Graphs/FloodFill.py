"""
Ref: https://leetcode.com/problems/flood-fill/description/

Note:
Compare with the source color not with 1

Intuition: 
"""

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
m=len(image)
n=len(image[0])
new_color = 2
source_color=image[sr][sc]

directions = ((0,-1),(-1,0),(0,1),(1,0))

def floodfilldfs():
    visited = set()
    visited.add((sr,sc))
    def dfs(node):
        
        i,j = node
        
        if image[i][j] != source_color:
            return

        image[i][j] = new_color
        for path in directions:
            rw=node[0] + path[0]
            cl=node[1] + path[1]
            
            if (rw,cl) in visited:
                continue

            if 0 <= rw < m and 0 <= cl < n and image[rw][cl] == source_color:
                visited.add((rw,cl))
                dfs((rw,cl))
    
    print("DFS Before",image)
    dfs((sr,sc))
    print("DFS After", image)

def floodfillbfs():
    visited = set()
    visited.add((sr,sc))

    print("Before BFS", image)

    from collections import deque
    que = deque()
    que.append((sr,sc))
    while que:
        i,j = que.popleft()
        
        if image[i][j] != source_color:
            continue

        image[i][j]=new_color
        for path in directions:
            rw = i + path[0]
            cl = j + path[1]

            if (rw,cl) in visited:
                continue
            
            if 0 <= rw < m and 0 <= cl < n and image[rw][cl] == source_color:
                que.append((rw,cl))
                visited.add((rw,cl))

    print("After BFS", image)    


floodfilldfs()
image=[[1,1,1],[1,1,0],[1,0,1]]
floodfillbfs()

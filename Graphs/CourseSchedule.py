"""
Ref: https://leetcode.com/problems/course-schedule/description/
"""

# Cyclic Graph
prereq = [[0,1], [0,2], [1,3], [1,4], [3,4]]
prereq=[[1,0],[0,1]]
n=2
adj = {i:[] for i in range(n)}

# convert to adjacent list
for cur,pre in prereq:
    adj[cur].append(pre)


visited = set()
def is_cyclic(node):
    if node in visited:
        return True

    if adj[node] == []:
        return False

    visited.add(node)

    # loop over the node's adjacent list
    for _node in adj[node]:
        if is_cyclic(_node):
            return True

    # Deleting current node from visited as other node treak it like cyclic
    # Keep the current node adjlist empty to prevent multiple DFS scan on same node
    visited.remove(node)
    adj[node] = []

    return False

can_take = True
for i in range(n):
    if is_cyclic(i):
        can_take = False
        break

print("Can Take Course", can_take)

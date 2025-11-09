"""
Ref: https://neetcode.io/solutions/graph-valid-tree
"""

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

# Plain adjlist
adjList = {p:[] for p in range(n)}

for cur, pre in edges:
    adjList[pre].append(cur)
    adjList[cur].append(pre)

visited = [None] * n

def is_valid_tree(node, prev):
    if visited[node] == 1:
        return False

    visited[node] = 1
    for _node in adjList[node]:
        print((_node, prev))
        if _node == prev:
            continue

        if not is_valid_tree(_node, node):
            return False

    return True


print("Is Valid Tree", is_valid_tree(0,-1))


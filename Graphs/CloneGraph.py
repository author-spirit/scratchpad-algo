"""
Ref: https://leetcode.com/problems/clone-graph/
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node.neighbors = [node2, node4]
node3.neighbors = [node2, node4]
node2.neighbors = [node, node3]
node4.neighbors = [node, node3]

dups = {}

def dfs(node, vis = set()):
    if not node or node.val in vis:
        return
    
    vis.add(node.val)
    for nd in node.neighbors:
        print(node.val, '-->' ,nd.val)
        dfs(nd, vis)

def duplicate(vertex):
    if vertex.val in dups:
        return dups[vertex.val]

    clone = Node(vertex.val)
    dups[vertex.val] = clone

    for nd in vertex.neighbors:
        clone.neighbors.append(duplicate(nd))

    return clone

print("Original")
dfs(node)

print("Duplicate")
dup = duplicate(node)
dfs(dup, set())


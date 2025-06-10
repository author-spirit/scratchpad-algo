class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 1 + MAX(L, R) method
def depth(node, left = 0, right = 0):

    if node == None:
        return 0
    
    mx_left = depth(node.left, left, right)
    mx_right = depth(node.right, left, right)

    return 1 + max(mx_left, mx_right)
    

def get_max_depth(tree):
    """
    Pseudocode – BFS Style (No Recursion)
    If the tree is empty, return depth = 0.

    Initialize a queue and put the root node into it.

    Set depth = 0

    While the queue is not empty:

    Determine how many nodes are at the current level (level_size = length of the queue).

    Loop through all nodes at this level:

    Remove the front node from the queue.

    If this node has a left child, add it to the queue.

    If it has a right child, add it to the queue.

    After finishing this level, increment depth by 1

    When the queue is empty, return depth.
    """

    # Similar to insertion sort
    if not tree:
        return 0

    queue = [tree]
    level = len(queue)
    depth = 0

    while level:

        node = queue.pop(0)
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        level -= 1
        if level == 0:
            depth += 1
            level = len(queue)
    
    return depth

node = Node(3)
node.left = Node(9)
node.right = Node(20)
node.right.left = Node(15)
node.right.right = Node(7)

from collections import deque
d = deque()
d.append(node)

count = 0
while d:
    thenode = d.popleft()
    if thenode.left:
        d.append(thenode.left)
    if thenode.right:
        d.append(thenode.right)
    count+=1

print(count)


import sys
sys.exit()


l = get_max_depth(node)
print(l)




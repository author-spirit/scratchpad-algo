# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
root = Node(10)
root.left = Node(20)
root.left.left = Node(40)
root.left.right = Node(50)
root.right = Node(30)
root.right.left = Node(60)
root.right.left.right = Node(70)

queue = []
traverse = []
sub = []
queue_size = 1

while root is not None:
    if root.left is not None:
        queue.append(root.left)

    if root.right is not None:
        queue.append(root.right)

    # Keep adding the element to sub array
    sub.append(root.val)

    # Once sub array is full and matches the previously calculated queue size then
    # append the sub array to main array
    # Get the new queue size
    if queue_size == len(sub):
        traverse.append(sub)
        queue_size = len(queue)
        sub = []
    
    root = queue.pop(0) if len(queue) else None

print(traverse)



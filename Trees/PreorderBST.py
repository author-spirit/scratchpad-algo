# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Easy

"""
stack
until node left
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
node = Node(1)
node.left = Node(-1)
node.left.left = Node(-2)
node.left.left.left = Node(-3)

node.right = Node(2)
node.right.left = Node(3)

def traverse(tree):

    stack = []
    arr = []
    
    node = tree
    stack.append(node)

    while len(stack) != 0:
        node = stack.pop()
        arr.append(node.val)

        # this comes next
        if node.right != None:
            stack.append(node.right)

        # this comes first
        if node.left != None:
            stack.append(node.left)
        
    return arr
        
arr = traverse(node)
print(arr)
        

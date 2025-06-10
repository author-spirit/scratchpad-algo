
"""
stack
until node left
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(tree):
    stack = [tree]

    # pop the stack
    arr = []

    while stack:
        root = stack.pop()
        if not root:
            break

        # First left then right
        if root.right:
            stack.append(root.right)
        
        if root.left:
            stack.append(root.left)
    
    return arr

def inorder(tree):

    # Move the far left
    # when it is null stop and add to list
    # now pop and move the root
    stack = [tree]
    arr = []

    while stack:
        node = stack[len(stack)-1]

        if node.left:
            stack.append(node.left)
            continue
            
        arr.append(node.val)
        
        # temp = stack.pop()
        # arr.append(temp.val)

        # if temp.right:
        #     stack.append(temp.right)
    
    return arr

def postorder(tree):
    
    stack = [tree]
    arr = []

    node = tree

    """
    node - [3,4,5,6,7]
    pop - 
    """
    
    while stack:
        
        # get me left most first
        while node.left:
            node = node.left
            if node:
                stack.append(node)
    
        node = stack.pop()

        print(stack, node.val)

        if node.right:
            stack.append(node.right)

        arr.append(node.val)

    return arr
    
node = Node(1)
node.left = Node(2)
node.right = Node(7)
node.left.left = Node(3)
node.left.right = Node(4)
node.left.right.left = Node(5)
node.left.right.right = Node(6)

print("")
arr = preorder(node)
print(arr)

print("Inorder")
arr = postorder(node)
print(arr)
        

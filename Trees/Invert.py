from Tree import Tree

root = Tree(4)
root.left = Tree(2)
root.right = Tree(7)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right.left = Tree(6)
root.right.right = Tree(9)

def invert(node):
    """que = []
    que.append(node)
    while que:
        curr = que.pop(0)
        curr.left, curr.right = curr.right, curr.left
        if curr.left:
            que.append(curr.left)
        if curr.right:
            que.append(curr.right)

    return node
    """

    if not node:
        return None
    node.left,node.right = invert(node.right), invert(node.left)
    return node

def display(root):
    node = root
    Tree.display(node)

print("Before")
display(root)
print("Inverting")
root = invert(root)
print("After")
Tree.display(root)


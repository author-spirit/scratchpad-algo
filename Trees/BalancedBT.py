from Tree import Tree

root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(3)
root.left.left.left = Tree(3)
root.left.left.right = Tree(3)

balanced = [True]

# DFS - InOrder
def height(node):
    if not node:
        return 0

    left = height(node.left)
    if not balanced[0]:
        return 0

    right = height(node.right)
    
    if abs(left-right) > 1:
        balanced[0] = False
        return 0

    return 1 + max(left, right)


def is_balanced(node):
    if not node:
        return False
    
    que = []
    que.append(node)
    while que:
        curr = que.pop(0)
        hl = height(curr.left)
        hr = height(curr.right)
        if abs(hl - hr) > 1:
            return False

        if curr.left:
            que.append(curr.left)

        if curr.right:
            que.append(curr.right)
    
    return True
    
    
height(root)
print(balanced)

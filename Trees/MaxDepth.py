from Tree import Tree

root = Tree(1)
root.left = Tree(3)
root.right = Tree(5)
root.left.left = Tree(7)
root.left.right = Tree(8)
root.right.left = Tree(9)
root.left.left.left = Tree(13)

node = root
Tree.inorder(node)

print("Height: ", Tree.height(node))

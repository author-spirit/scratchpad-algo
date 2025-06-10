from Tree import Tree

p = Tree(10)
p.left = Tree(20)
p.left.right = Tree(30)

q = Tree(10)
q.left = Tree(20)
q.left.left = Tree(30)

same = [True]
def is_same(node1, node2):
    if not node1 or not node2:
        return None

    is_same(node1.left, node2.left)
    if node1.val != node2.val:
        same = [False]
        return None

    is_same(node1.right, node2.right)

is_same(q,q)
print(same)
    

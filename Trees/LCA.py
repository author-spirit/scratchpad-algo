"""
https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
"""

from Tree import Tree

root = Tree(6)
root.left = Tree(2)
root.right = Tree(8)
root.left.left = Tree(0)
root.left.right = Tree(4)
root.left.right.left = Tree(3) 
root.left.right.right = Tree(5) 

root.right.left = Tree(7) 
root.right.right = Tree(9) 


def iterative_way(root):
    def lca(root, target):
        node = root
        traverse = []
        while node:
            traverse.append(node)
            if node.val == target.val:
                break
            if target.val > node.val:
                node = node.right
            else:
                node = node.left

        return traverse

    p1 = lca(root,root.left)
    p2 = lca(root,root.left.right)

    n = min(len(p1), len(p2))

    common = None
    for i in range(n):
        if p1[i].val == p2[i].val:
            common = p1[i]

    print("Common", common, common.val)

def optimal_way(root, p, q):
    def lca(root,p,q):
        node = root
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node
        return node

    thenode = lca(root, p,q)
    print("The LCA is: ",thenode.val)

optimal_way(root,root.left, root.left.right)



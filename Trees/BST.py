# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(node):
    if node is None:
        return
    
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

def preorder(node):
    if node is None:
        return
    
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.val,end=" ")

def create_bst(items):

    root = None
    queue = []
    is_left = True
    for i in items:
        node = Node(i)

        if not queue:
            root = node
        else:
            root = queue.pop(0)
            if is_left:
                root.left = node
            else:
                root.right = node

        queue.append()

def insert_node(root, n):
    node = root
    prev = None
    while node is not None:
        if node is None:
            break;

        prev = node
        if node.val > n:
            node = node.left
        else: node = node.right

    # conclude, we got previous, final check if prev > n then left else right
    if prev is not None:
        if prev.val > n:
            prev.left = Node(n)
        else:
            prev.right = Node(n)
    else:
        root = Node(n)
    
    return root

# https://leetcode.com/problems/delete-node-in-a-bst/
def remove_node(node, n):
    if not node:
        return None
    
    if node.val == n:
        # if no children
        if not node.left and not node.right:
            return None

        # If root has no left then return right
        if not node.left:
            return node.right
        
        if not node.right:
            return node.left
        
        # Both children

        # Get far left
        temp = node.right
        while temp.left != None:
            temp = temp.left

        # Replace the successor value
        node.val = temp.val

        # still we need to remove the the successor node
        node.right = remove_node(node.right, temp.val)
    
    if node.val > n:
        node.left = remove_node(node.left, n)
    else:
        node.right = remove_node(node.right,n)

    # Final processed
    return node
    
def search_node(root, k):
    node = root
    while node is not None:
        if node.val == k:
            return node
        
        if root.val > k:
            node = node.left
        else:
            node = node.right
    return node

# My style
def delete_node(root, k):
    if not root:
        return None

    node = root
    prev = root
    
    while node != None:

        # Node match
        if node.val == n:
            
            # no children
            if not node.left and not node.right:
                node = None
                break
            
            # If 1 or 2 children
            if not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            elif node.right and node.left:

                # far right only no need of left
                temp = node.right
                far_left = get_successor(node.right)

                # Update the successor value
                node.val = far_left.val

                # Delete the sucessor



        
        # If no children

def get_successor(node):
    if not node.left:
        return node

    return get_successor(node.left)

def get_predecessor(node):
    if not node.right:
        return node.val
    
    return get_predecessor(node.right)

# TODO, [5,3,6,2,4,null,7]
# [5,4,6,2,7]

def split_bst(node):
    pass

root = Node(5)
root = insert_node(root, 3)
root = insert_node(root, 6)
root = insert_node(root, 2)
root = insert_node(root, 4)
root = insert_node(root, 7)

root = remove_node(root, 3)

# print(root.val, root.left, root.right.val)

print("Pre", end=" ")
preorder(root)
print()
print("In", end=" ")
inorder(root)
print()
print("post", end=" ")
postorder(root)
print()



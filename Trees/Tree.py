class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    
    @staticmethod
    def inorder(node):
        if not node:
            return None

        Tree.inorder(node.left)
        print(node.val)
        Tree.inorder(node.right)
    
    @staticmethod
    def height(node):
        if not node:
            return 0
        
        return 1 + max(Tree.height(node.left), Tree.height(node.right))
        
    @staticmethod
    def display(node):
        que = []
        que.append(node)
        while que:
            curr = que.pop(0)
            print(curr.val)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

"""
Ref: https://leetcode.com/problems/path-sum/description/
"""

class Node:
    def __init__(self,n):
        self.val = n
        self.left = None
        self.right = None

node = Node(1) #5
node.left = Node(2) #4
"""node.right = Node(8)
node.left.left = Node(11)
node.left.left.left = Node(7)
node.left.left.right = Node(3)

node.right.left= Node(13)
node.right.right= Node(4)
node.right.right.right= Node(1)
"""
target=22
def backtrack(node,sum):
    if not node:
        if sum == target:
            return True
        return False

    
    res = backtrack(node.left, sum + node.val)
    if res:
        return True
    
    return backtrack(node.right, sum+node.val)

res = backtrack(node,0)
print(res)
    

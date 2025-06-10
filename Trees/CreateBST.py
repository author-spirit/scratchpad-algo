# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

items = [8,5,1,7,10,12]

"""
I need preorder & inorder to make new BST
"""
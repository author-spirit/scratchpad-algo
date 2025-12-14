# I just need a variable for data, next that's it, the next points to preceding node so
# so I can just point the same class to next

import sys

class Node:
    def __init__(self, data, node=None):
        self.data = data
        self.next = node

def insert_head(data, node):
    first = Node(data, node)
    return first

def delete_head(node):
    first = node
    next = node.next
    del first
    return next

def delete_node(node, element):

    prev = node
    next = None

    # Traverse and match the element
    # Keep track of prev and next nodes
    # If match found then get the next node
    # That's it done. Update the prev's pointer with next node

    while node.next is not None:
        if node.data == element:
            next = node.next
            break

        prev = node

        # Next iterate
        node = node.next

    prev.next = next

def delete_node_position(node, pos):

    prev = node
    next = None

    # If matched index then get next node and update prev next pointer with next node

    i = 0
    while node.next is not None:
        if i == pos:
            next = node.next
            print(next.data)
            break
        
        prev = node

        node = node.next # next node

        i=i+1

    prev.next = next

def reverse(node):
    prev = None
    next = node

    while node != None:
        next = node.next

        # Store the prev node in current node's next
        # update previous as current node for preceding node 
        # i.e 1[x], 2[1]
        node.next = prev
        prev = node

        # move next to node
        node = next
    
    return prev


def printLL(node):
    temp = node
    while temp != None:
        print(temp.data)
        temp = temp.next

node = Node(10)
node.next = Node(25)
node.next.next = Node(34)
node.next.next.next = Node(45)
node.next.next.next.next = Node(51)
node.next.next.next.next.next = Node(66)

printLL(node)
node = reverse(node)
print("Reversed")
printLL(node)
sys.exit(0)

node = delete_head(node)
node = insert_head(5,node)


# delete_node(node,34)
delete_node_position(node,0)
print("=====")

# four = node.next.next.next
# del four

printLL(node)

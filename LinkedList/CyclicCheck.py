# I just need a variable for data, next that's it, the next points to preceding node so
# so I can just point the same class to next

class Node:
    def __init__(self, data, node=None):
        self.data = data
        self.next = node

def is_cylic(node):
    fast = node # Every 2 steps i.e next of next
    slow = node # 1 step
    cyclic = False

    # Keep Looping until fast/slow becomes None
    # Why fast required is to stop attempting 2 steps
    while fast != None and slow != None and fast.next != None:
        fast = fast.next.next # 2 next forward
        slow = slow.next

        if fast == slow:
            return fast
    
    return None

# Tortoise method
def cyclic_length(node):
    slow = node;
    fast = node;

    count = 0
    while slow != None and fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        count = 1
        if slow == fast:
            slow = node
            while slow != fast:
                slow = slow.next
                fast = fast.next

            # Restart from matched position
            while fast.next != slow:
                count = count + 1
                fast = fast.next

            break

    return count


val = [10,25,34,45,51,66,25]

node = Node(10)
node.next = Node(25)
node.next.next = Node(34)
node.next.next.next = Node(45)
node.next.next.next.next = Node(51)
node.next.next.next.next.next = Node(66)
node.next.next.next.next.next.next = node.next

print("Cyclic Node Length: ", cyclic_length(node))

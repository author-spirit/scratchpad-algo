# In Double linked list there are prev, data and next pointer

class Node:

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

def custom_round(value):
    return int(value + 0.5) if value > 0 else int(value - 0.5)

def reverse(node):
    # auxiliary spaces
    head = node

    import time

    while head != None:
        temp = head.prev
        head.prev = head.next
        head.next = temp

        if temp != None:
            print(temp.prev.data)
        # print(temp.data)
        head = head.prev

    print("===")
    return temp.prev
    

node = Node(10)
node.prev = None

# Second 
node.next = Node(15)
node.next.prev = node

# Thrid
node.next.next = Node(20)
node.next.next.prev = node.next

# Fourth
node.next.next.next = Node(25)
node.next.next.next.prev = node.next.next

# Fifth
node.next.next.next.next = Node(30)
node.next.next.next.next.prev = node.next.next.next

node = reverse(node)
while node != None:
    print(node.data)
    node = node.next
 


# Improvised Way

# length = 0
# while node is not None:
#     # print(node.data, node.prev.data if node.prev is not None else None)
#     length = length + 1
#     node = node.next

# # If length is odd we get absolute mid, else get mid add 1 for that
# mid = custom_round(length/2) - 1
# if length % 2 == 0:
#     mid = mid + 1

# print(mid)

# i = 0
# while head is not None:
#     if(i==mid):
#         break

#     head = head.next
#     i = i+1

# print(head.data)




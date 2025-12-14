class Node:
    def __init__(self, data, node = None):
        self.data = data
        self.next = node
    
def printLL(node):
    head = node
    while head != None:
        print(head.data)
        
        head = head.next

def palindrome(node):
    tail = node
    collect = []

    while tail != None:
        collect.append(tail.data)
        tail = tail.next

    is_palindrome = True

    i=0
    j=len(collect) - 1
    while i <= j:
        if collect[i] != collect[j]:
            is_palindrome = False
            break
        i = i+1
        j = j-1
    
    print(is_palindrome)

def reverse(node):
    prev = None
    temp = node
    while temp != None:
        next = temp.next
        temp.next = prev
        prev = temp

        temp = next

    return prev
    

node = Node(10)
node.next = Node(20)
node.next.next = Node(30)
node.next.next.next = Node(20)
node.next.next.next.next = Node(10)

# printLL(node)
# reverse(node)
palindrome(node)



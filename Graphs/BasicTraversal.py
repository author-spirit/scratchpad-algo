class Node:
    def __init__(self,num):
        self.num = num
        self.next = []

graph = Node(1)
graph.next.append(Node(2))
graph.next.append(Node(4))

graph.next[0].next.append(Node(3))

graph.next[1].next.append(Node(5))

graph.next[1].next[0].next.append(Node(3))

# Traverse
seen = set()
def backtracking(node):
    if node.num in seen:
        return

    print(node.num)
    seen.add(node.num)
    for n in node.next:
        if n.num in seen:
            continue

        backtracking(n)

def stack_traverse():
    seen = set()
    stack = [graph]
    while stack:
        node = stack.pop()
        if node.num in seen:
            continue
    
        print(node.num)
        seen.add(node.num)
        for n in node.next:
            stack.append(n)

def bfs():
    seen = set()
    queue = [graph]
    while queue:
        node = queue.pop(0)
        if node.num in seen:
            continue

        print(node.num)
        seen.add(node.num)
        for n in node.next:
            queue.append(n)

print("DFS: Bactracking")
backtracking(graph)

print("DFS: Stack Traverse")
stack_traverse()

print("BFS: Queue")
bfs()

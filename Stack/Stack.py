class Stack:

    def __init__(self):
        self.value = []

    def push(self, value):
        self.value.append(value)

    def pop(self):
        value = self.value[-1]
        del self.value[-1]
        return value
    
    def view(self):
        return self.value[-1]

    def display(self):
        for i in self.value[::-1]:
            print(i)

    
    def clear(self):
        self.value = []

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
stack.pop()
print(stack.view())

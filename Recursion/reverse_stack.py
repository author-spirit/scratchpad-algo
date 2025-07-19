stack = [1,2,3,4,5]

def reverse(stack):
    if not stack:
        return stack

    val = stack.pop()
    reverse(stack)
    print("Printing")
    insert(stack, val)

def insert(stack, val):
    print("Insert", stack, val)
    if not stack:
        stack.append(val)
        return
    
    stack_val = stack.pop()
    insert(stack,val)
    stack.append(stack_val)

print("Before", stack)
reverse(stack)
print("After", stack)

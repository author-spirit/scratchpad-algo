stack = [1,7,3,2,5]

def sortstack(stack, num = None):
    if not stack:
        return
    
    num = stack.pop()
    sortstack(stack,num)
    merge(stack, num)

def merge(stack, num):
    if not stack or stack[-1] <= num:
        stack.append(num)
        return

    val = stack.pop()
    merge(stack, num)
    stack.append(val)

print("Before", stack)
sortstack(stack)
print("After", stack)

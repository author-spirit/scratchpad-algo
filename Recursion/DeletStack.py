stack = [1,2,3,4,5]

def deletemid(stack,mid):
    if not stack:
        return
    
    num = stack.pop()
    if mid == 1:
        return

    deletemid(stack, mid-1)
    stack.append(num)


print("Before", stack)
deletemid(stack, 2)
print("after", stack)

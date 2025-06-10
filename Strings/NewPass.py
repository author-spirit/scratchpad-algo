password = "amoma"
new_password = list(password)

l=0
r=len(new_password)-1

visited = {}
count = 0

while l < r:
    right = new_password[r]
    left = new_password[l]

    if right == left:
        visited[right] = 1
    else:
        if right not in visited:
            new_password[r] = left
            visited[right] = 1
        elif left not in visited:
            new_password[l] = right
            visited[left] = 1
        count +=1
    l +=1
    r -=1

print(count, "".join(new_password))
            

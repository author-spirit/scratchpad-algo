arr = [4,-1,2,-7,3,4]

l = 0
r = 0

curr = 0
mx = arr[0]

for i in range(len(arr)):
    curr = curr + arr[i]
    if curr < 0:
        curr = 0
    
    mx = max(mx, curr)

print(mx)
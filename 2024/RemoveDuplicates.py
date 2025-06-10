arr = [0,0,1,1,1,2,2,3,3,4]

i = 0
j= 1
while j < len(arr):
    if arr[j] != arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j += 1
    
print(arr)

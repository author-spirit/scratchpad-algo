arr = [31, 90, 10, 67, 7, 23, 10]

for i in range(len(arr) -1):
    isSwapped = False
    for j in range(len(arr) - i -1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            isSwapped = True
    
    # If no swap happended then it already sorted
    if not isSwapped:
        break

print(arr)
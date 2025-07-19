arr = [13,46,24,52,20,9]

def sort(arr, i, j):
    if i == len(arr):
        return arr 

    # reset
    if j == len(arr):
        i += 1
        j = i
    else:
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    
    return sort(arr, i, j)


arr = sort(arr, 0, 0)
print(arr)

assert sorted(arr) == arr, "Array not sorted"
arr = [13,46,24,52,20,9]

def sort(arr, i = 0, j = 0):
    if i == len(arr):
        return arr 

    # reset
    if (j-1) < 0:
        i += 1
        j = i
    else:
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
    
    return sort(arr, i, j)


arr = sort(arr,1,1)

assert sorted(arr) == arr, "Array not sorted"
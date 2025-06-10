def binary_search(arr, needle):
    low, high = 0, len(arr)-1
    
    for i in range(len(arr)):
        mid = int(low + (high - low)/2)
        print(mid, arr[mid])

        if arr[mid] == needle:
            return mid
        
        if needle > arr[mid]:
            low = mid + 1
        
        if needle < arr[mid]:
            high = mid - 1

arr = [1]
print(binary_search(arr, 1))
    

def search(arr, low, high, target):
    # base case
    if low > high:
        return -1
    
    mid = int((low + high)/2)
    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        high = mid-1
    else:
        low = mid+1
    
    print(low, mid, high)
    return search(arr, low, high, target)

arr = [10,20,30,50,73, 73,75,91]
res = search(arr, 0, len(arr)-1, 30)
print(res, arr[res])
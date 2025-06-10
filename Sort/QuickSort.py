

arr = [5,1,-2,2,2]

def sort(arr, low, high):
    if low >= high:
        return

    pivot = partition(arr, low, high)
    sort(arr,low,pivot-1)
    sort(arr,pivot+1, high)

def partition(arr, low, high):
    pivot = arr[high] # to be random
    p = low # this will be actual pivot position index
    for i in range(low, high + 1):
        if pivot > arr[i]:
            # swap
            arr[p], arr[i] = arr[i], arr[p]
            p +=1 
    
    arr[p], arr[high] = arr[high], arr[p]
    
    return p

print("Before", arr)
sort(arr, 0, len(arr)-1)
print("After", arr)
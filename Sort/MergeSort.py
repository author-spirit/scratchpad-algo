arr = [4, 1, 3, 9, 7]

def sort(arr, low, high, dir = ""):
    if low >= high:
        return
    
    mid = int((low+high)/2)
    sort(arr, low, mid, "left")
    sort(arr, mid+1, high, "right")
    merge(arr, low, high, mid)

def merge(arr, low, high, mid):
    aux = []
    i = low
    j=mid+1

    while i < mid + 1 and j < high + 1:
        if arr[i] > arr[j]:
            aux.append(arr[j])
            j += 1
        else:
            aux.append(arr[i])
            i += 1
    
    while i < mid + 1:
        aux.append(arr[i])
        i += 1
    
    while j < high + 1:
        aux.append(arr[j])
        j += 1
    
    print(aux)
    k = low
    for i in aux:
        arr[k] = i
        k += 1
    
print("Before", arr)
sort(arr, 0, len(arr)-1)
print("After", arr)
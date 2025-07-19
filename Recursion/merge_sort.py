arr = [1.00001,1, 5, 9, 2, 6, 10,10,10.5]

def mergesort(arr, start=0, end=0):
    if not arr:
        return
    
    if start >=end:
        return

    partition = int((start+end)/2)
    mergesort(arr, start, partition)
#    print(start,partition,end)   
    mergesort(arr, partition+1, end)
    # merge original array
    merge(arr, start, end, partition)

def merge(arr, start, end, partition):
    arr1 = arr[start:partition+1]
    arr2 = arr[partition+1:end+1]
    arr3 = []
    
    a1 = 0
    a2 = 0
    left = start
    
    while a1 < len(arr1) and a2 < len(arr2):
        if arr1[a1] <= arr2[a2]:
            arr[left] = arr1[a1]
            a1 +=1
        else:
            arr[left] = arr2[a2]
            a2 +=1
        left=left+1
    
    print("A1", a1, len(arr1))
    while a1 < len(arr1):
        arr[left]=arr1[a1]
        left+=1
        a1 = a1+1
    
    print("A2", a2, len(arr2))
    while a2 < len(arr2):
        arr[left]=arr2[a2]
        left+=1
        a2+=1
    
    print((start, partition, end), arr1, arr2, arr3, arr)
    
print("Before", arr)
mergesort(arr, 0, len(arr))
print("After", arr)





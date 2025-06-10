"""
divide-conqueue method
1. Get the pivot - last index of an array
2. Push values to left of pivot value if they are lower
3. Push values to right most if pivot value is greater
4. Return back the actual pivot value's index
B. Split the array into two and let it run in recurssion till low >= high
"""
import time
import random

def partition(arr, low, high):
    pivot_index = random.randint(low,high)
    pivot = arr[pivot_index]
    pos = low

    for i in range(low, high+1):
        if arr[i] <= pivot:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    arr[pos], arr[high] = arr[high], arr[pos]
    
    return pos
    

def quicksort(arr, low, high):
    if low >= high:
        return
    
    pivot = partition(arr, low, high)
    quicksort(arr, low, pivot-1)
    quicksort(arr, pivot + 1, high)

arr = [5,3,1,7,2]
quicksort(arr, 0, len(arr)-1)
print(arr)
intervals = [[1,3],[6,9]]
newInterval = [2,5]

clean_intervals = intervals

def placement():
    low = 0
    high = len(clean_intervals)-1
    while low < high:
        mid = int((low + high)/2)
        intervalA = clean_intervals[mid][0]
        if intervalsA > newInterval[0]:
            clean_intervals[mid] = merge_arrays(clean_intervals[mid], newInterval)
            break

def merge_arrays(array1, array2):
    
    a1 = 0
    a2 = 0

    new_array = []
    
    while a1 < len(array1) and a2 < len(array2):
        if array1[a1] <= array2[a2]:
            new_array.append(array1[a1])
            a1+=1
        else:
            new_array.append(array2[a2])
            a2+=1
    while a1 < len(array1):
        new_array.append(array1[a1])
        a1+=1
    
    while a2 < len(array2):
        new_array.append(array2[a2])
        a2+=1
    
    return new_array

print(merge_arrays([1,3], [4,7]))

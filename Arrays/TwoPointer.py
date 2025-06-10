arr = [7,11,14,22,31]

t = 33

def optimal(arr, t):
    prev = {}
    for i in range(len(arr)):
        curr = arr[i]
        diff = t-curr
        if prev.get(diff, -1) !=-1:
            return [prev[diff],i]
        prev[curr] = i
    return []

print(optimal(arr, t))


def brute_force(arr, t):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum = arr[i] + arr[j]
            if sum == t:
                return [arr[i], arr[j]]
    return []


"""
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
"""

arr = [5,3,2,1,8,7]

"""
Insertion sort: Think this as playing card.
"""

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break # if no longer swap available

# ==============================

# Insertion sort by keys
# Another example for K-Frequent items

items = list({4:1, 2:2, 3:1, -1:2}.items())
vals = []

for i in range(1, len(items)):
    for j in range(i,-1,-1): # reverse check
        if items[j][1] > items[j-1][1]:
            items[j], items[j-1] = items[j-1], items[j]
        else:
            break

k = 2
for i in range(k):
    vals.append(items[i][0])

print("After", vals)
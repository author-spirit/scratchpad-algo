arr = [2,2,1,1,1,2,2]

freq = {}

for n in arr:
    freq[n] = freq.get(n, 0) + 1

majority = int(len(arr)/2) # 1

element = 0
for (k, v) in freq.items():
    if v > majority:
        element = k

print(element)

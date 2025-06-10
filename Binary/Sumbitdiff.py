arr = [13,23,12]

pairs = []

sum = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        #pairs.append([arr[i], arr[j]])
        pairs.append(arr[i] ^ arr[j])
print(pairs)

for pair in pairs:
    value = pair
    occur = 0
    while value !=0:
        value = value & (value-1)
        occur +=1
    sum += occur

print(sum)

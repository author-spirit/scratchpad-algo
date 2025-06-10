s = "a"

freq = {}
for c in s:
    freq[c] = freq.get(c, 0)+1

sum = 0
counts = {}
for count in freq.values():
    counts[count] = counts.get(count, 0)+1
    if count == 1:
        continue;
    sum += count

# If sum is even, add 1 else
if counts[1] and sum % 2 ==0:
    sum +=1

print(sum)

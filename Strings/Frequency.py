freq = {}

s = 'My good Old friend (拼音拼音拼音拼音)'

for c in s:
    if not c.strip():
        continue
    char = c.lower() if c.isascii() else c
    freq[char] = freq.get(char, 0) + 1
    
print(freq)

count = freq.values()

maxcount = ['',0]
mincount = ['',float('inf')]

for f in freq:
    if freq[f] > maxcount[1]:
        maxcount[1] = freq[f]
        maxcount[0] = f
        
    if freq[f] < mincount[1]:
        mincount[1] = freq[f]
        mincount[0] = f

print(maxcount, mincount)

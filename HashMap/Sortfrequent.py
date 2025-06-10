import heapq

s = "abbbaacacf"

freq = {}
for c in s:
    freq[c] = freq.get(c, 0)+1

# Put the count in priority queue
data = [(-count,char) for (char, count) in freq.items()]
heapq.heapify(data) # Max heap

text = ""
while data:
    char_data = heapq.heappop(data)
    char = char_data[1]
    count = -(char_data[0])
    text = text + char * count

print(text)

import sys
sys.exit()


# Iterate all the stored frequency counts
max_count = 0
sorted_text = ""
for (num, count) in freq.items():
    cloned_text = "".join([num]*count)
    print("CT",cloned_text)
    
    # Prefix, adds max frequency in begining of sorted_text
    if count >= max_count:
        sorted_text = cloned_text + sorted_text
        max_count = count
    else:
        sorted_text = sorted_text + cloned_text

print(sorted_text)

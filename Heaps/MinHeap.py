

import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

print("heap: ",heap)

# to pop the smallest element
small = heapq.heappop(heap)
print("smallest: ", small)

# convert list to heap
vals = [10, 12, 11, 34, 8, 2]
heapq.heapify(vals)
print("Heapify", vals)

# get nlargest, nsmallest
large_3 = heapq.nlargest(3,vals)
print("Largest 3", large_3)

# Pairs: heaps can accepts items in
# tuple, where item[0] treated as priority
# tuple --> (priority, val)
# lowest priority number == highest priority
# e.g (10,1), (1,10) -> (1,10) comes first
pairs = [(10,1), (2,10), (1,30)]
heapq.heapify(pairs)
print("Heap in pairs: ", pairs)

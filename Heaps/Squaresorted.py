import heapq

nums = [-7,-3,2,3,11]

heap = []

for n in nums:
    sq = n**2
    heapq.heappush(heap, sq)

sorted = []
while heap:
    sorted.append(heapq.heappop(heap))

print(sorted)

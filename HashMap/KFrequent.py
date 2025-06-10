nums = [4,1,-1,2,-1,2,3]

k = 2

def get_top_freq(nums, k):
    if not nums:
        return []

    frequencies = {}
    for n in nums:
        if n not in frequencies:
            frequencies[n] = 1
        else:
            frequencies[n] = frequencies[n] + 1

    # sort based on frequency not the values in blind
    groups = {}

    for f in frequencies:
        freq = frequencies[f]
        if freq not in groups:
            groups[freq] = [f]
        else:
            groups[freq].append(f)
    
    counts = sorted(list(groups.keys()), reverse=True)
    vals = []
    for c in counts:
        if k == len(vals):
            break
            
        group = sorted(groups[c], reverse=True)
        vals.extend(group[:])

    return vals[:k] if k < len(vals) else vals


# better version
# https://neetcode.io/problems/top-k-elements-in-list
def get_topk(nums, k):

    # count the occurences
    counts = {}
    for i in nums:
        counts[i] = 1 + counts.get(i, 0)
    
    print(counts)

    # At to bucket
    # index is frequency
    # values are numbers
    # keep the bucket with empty placeholder of len(nums) 
    # bucket = [[]] * len(nums) # Each sub index are shared amoung others !!
    bucket = [[] for i in range(len(nums)+1)] # Here 0 is negligible
        
    # Add to bucket
    for v,c in counts.items():
        bucket[c].append(v)

    # Now extract the k, descending order
    items = []
    for i in range(len(bucket)-1, -1, -1):
        for j in bucket[i]:
            items.append(j)

            if len(items) == k:
                return items
    
    return items

# top_k = get_top_freq(nums, k)
top_k = get_topk(nums, k)


print(top_k)

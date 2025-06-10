def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    vis = []
    items = []

    for i in range(len(strs)):
        if i in vis:
            continue
        sub = [strs[i]]
        active = "".join(sorted(list(strs[i])))
        for j in range(i+1, len(strs)):
            if active == "".join(sorted(list(strs[j]))):
                sub.append(strs[j])
                vis.append(j)
        
        if sub:
            items.append(sub)
            sub = []
        
    return items

def optimal(strs):
    items = {}
    n = len(strs)-1
    i = 0

    if len(strs) == 1:
        return [[strs[0]]]
    
    while i <= n:
        first = "".join(sorted(strs[i]))
        last = "".join(sorted(strs[n]))

        print(first, last)

        if first not in items:
            items[first] = [strs[i]]
        elif first in items:
            items[first].append(strs[i])
        
        if last not in items:
            items[last] = [strs[n]]
        elif last in items:
            items[last].append(strs[n])
        
        i=i+1
        n=n-1
    
    
    return list(items.values())

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
strs = ["","b",""]
print(optimal(strs))
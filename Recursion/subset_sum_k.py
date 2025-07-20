arr = [1,2,1]
k=2

"""
# Notes
==========
1. Include/Not Include
2. Jump to next element once done deciding
3. Compare with the sum K.
4. Store the subset in main list/aux

# Doubt
When k=3, the subset what I assumed [1,1,1] is not possible because I have only two 1(s)

# https://leetcode.com/problems/subsets/description/
"""

all_subsets = []
def subsets(i,subs=[]):    
    if i >= len(arr):
        if sum(subs) == k:
            all_subsets.append(subs.copy())
            return True
        return True

    if sum(subs) == k:
        all_subsets.append(subs.copy())
        return True
    elif subs:
        return False

    num = arr[i]

    # Include the number
    subs.append(num)
    if subsets(i+1, subs):
        return True
    
    subs.pop()
    if subsets(i+1, subs):
        return True

    return False
    
subsets(0)
print(all_subsets)

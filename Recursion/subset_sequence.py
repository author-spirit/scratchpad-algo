arr = [1,2,3]

"""
                1
            [1]   []
        [1,2]   [1]     [2]     []
[1,2,3]     [1,2]   [1,3]   [2,3]   [3]     []

# Notes
==========
1. Include/Not Include
2. Jump to next element once done deciding
3. Store the subset in main list/aux

# https://leetcode.com/problems/subsets/description/
"""

all_subsets = []
def subsets(arr,subs=[]):
    if not arr:
        all_subsets.append(subs.copy())
        return

    num = arr[0]

    # Include the number
    subs.append(num)
    print("INX", subs, num)
    subsets(arr[1:], subs)

    # Not include the number
    subs.pop()
    print("NOX", subs, num)
    subsets(arr[1:], subs)
    #all_subsets.append(subs)
    
subsets(arr)
print(all_subsets)

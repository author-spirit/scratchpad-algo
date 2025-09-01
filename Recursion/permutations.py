"""
Ref: https://leetcode.com/problems/permutations/

Nested Backtracking
"""


n=[1,2,3]

subsets = []
def bactrack(subset):
    if len(subset) == len(n):
        subsets.append(subset.copy())
        return

    for i in n:
        if i not in subset:
            subset.append(i)
            bactrack(subset)
            print(subset)
            subset.pop()

bactrack([])
print(subsets)
            

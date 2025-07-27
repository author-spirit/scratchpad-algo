"""
Combination Sum - II
Ref: https://leetcode.com/problems/combination-sum-ii/description/
"""

candidates = [10,1,2,7,6,1,5]
target = 8

subsets = []
def backtrack(i,subs=[]):
    if i == len(candidates):
        if sum(subs) == target:
            subsets.append(subs.copy())
        return

    # If Same add to subsets otherwise return
    if sum(subs) >= target:
        if sum(subs) == target:
            subsets.append(subs.copy())
        return
    
    subs.append(candidates[i])
    # Include
    next_index = i+1
    backtrack(next_index, subs)
    
    # Exclude, the above used number never show up
    subs.pop()
    while next_index < len(candidates) and candidates[next_index] == candidates[i]:
        next_index +=1
    print("Next", i, subs.copy(), next_index)
    backtrack(next_index, subs)

"""
i=0
next_index = 1
candidates.sort()
while next_index < len(candidates) and candidates[next_index] == candidates[i]:
    next_index +=1
print("Next", i, next_index)

from sys import *
exit()
"""

candidates.sort()
print(candidates)
backtrack(0)
print(subsets)

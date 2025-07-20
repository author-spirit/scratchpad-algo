"""
Ref: https://leetcode.com/problems/combination-sum/description/
"""

candidates = [2,3,6,7]
target=7

subsets = []
def backtrack(i=0,subset=[]):
    total = sum(subset)
    if i==len(candidates):
    # matches when end of candidates 
        if total == target:
            subsets.append(subset.copy())
        return
            
    # Exit when subset reached beyond the target
    if total > target:
        return

    # Early match
    if total == target:
        subsets.append(subset.copy())
        return 

    # Include the same candidate unlimited times but on base case
    subset.append(candidates[i])
    backtrack(i, subset)

    # Skip the above added value completely. Add use next value
    subset.pop()
    backtrack(i+1,subset)
        
backtrack()
print(subsets)

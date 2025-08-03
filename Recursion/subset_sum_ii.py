"""
Ref: https://leetcode.com/problems/subsets-ii/description/
"""


n=3
arr = [1,2,2]

subsets = []
def backtrack(i,subs):
    if i==len(arr):
        subsets.append(subs.copy())
        return
    
    subs.append(arr[i])
    backtrack(i+1, subs)
    
    num = subs.pop()
    i+=1
    while i < len(arr) and num == arr[i]:
        i+=1
    
    print("Second", i)
    backtrack(i, subs) 

backtrack(0,[])
print(subsets)

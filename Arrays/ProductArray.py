"""
https://leetcode.com/problems/product-of-array-except-self/
Time Taken: 2 days
Revisit: 17 April
Pattern: Prefix Sum
"""

nums = [-1,1,0,-3,3]

# Doesn't scale for large data
# Division method
def brute(nums):
    arr = []

    sum = 1
    for i in range(len(nums)):
        sum *= nums[i]
    
    for i in range(len(nums)):
        arr.append(int(sum/nums[i]))
    
    return arr

def optimal(nums):
    arr = []

    for i in range(len(nums)):
        if i == 0:
            prefix = 1
        else:
            prefix = arr[i-1] * nums[i-1] 
        arr.append(prefix)
    
    n = len(nums) - 1
    for i in range(n, -1, -1):
        arr[n-i] = arr[i] * nums[i]
    
    return arr
    

print(optimal(nums))
            
    
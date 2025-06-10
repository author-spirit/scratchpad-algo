# https://leetcode.com/problems/two-sum/description/

nums = [7,1,-1,2]
target = 3
# O(n)

# Differences, key holds the difference of target and value be the index
# Extended, get the number of count that matched the target.
def get_target_count(nums, target):
    count = 0
    differences = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if nums[i] in differences:
            count = 1
        
        differences[diff] = i
    
    return []

def get_two_sum(nums, target):
    visited = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in visited:
            return [visited[diff], i]
        visited[nums[i]] = i
    return []

print(get_two_sum(nums, target))




# Keep hold of high value
# Update the high only when next value is greater
# 

def max(nums, i):
    if i == len(nums):
        return 0
    
    # compare the curr and next
    # get next value by recursion
    # in recursion state 
    if nums[i] < max(nums, i+1):
        return nums[i+1]

    return nums[i]

high = max([17,12,25], 0)
print(high)
nums = [45192,0,-659,-52359,-99225,-75991,0,-15155,27382,59818,0,-30645,-17025,81209,887,64648]
a1=0
a2=0

# sliding window - variable size
while a2 < len(nums):
    if nums[a1] == 0 and nums[a2] !=0 and nums[a1] != nums[a2]:
        nums[a1], nums[a2] = nums[a2], nums[a1]
        a2+=1
        a1+=1
    elif nums[a1] !=0:
        a1+=1
        a2=a1+1
    else:
        a2+=1

print(nums)

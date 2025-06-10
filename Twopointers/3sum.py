nums = [-1,0,1,2,-1,-4]

nums = sorted(nums)
print(nums)

l=1
r=len(nums)-1
fixed=0
arr = []

while l < r:
    sum = nums[fixed] + nums[l] + nums[r]
    if sum == 0:
        arr.append([nums[fixed], nums[l], nums[r]])
        r-=1
    else:
        l+=1
        fixed+=1

print(arr)



nums = [3,0,1]

def enumeration(nums):
    nums = sorted(nums)

    for i,v in enumerate(nums):
        if i != v:
            return i

def sum_diff(nums):
    return sum(range(len(nums)+1)) - sum(nums)

print(sum_diff(nums))

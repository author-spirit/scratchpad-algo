# April 13

nums = [5, 3, -2, 0, 7, -10, 4]

def bubble1(nums, np, is_min = False):
    parent = 0 if (np-1) <= 0 else (np-1)//2
    if is_min and nums[parent] <= nums[np]:
        return nums
    
    if not is_min and nums[parent] >= nums[np]:
        return nums
    
    nums[parent], nums[np] = nums[np], nums[parent]
    np = parent
    return bubble(nums, np, is_min)

def bubble(nums, np, is_min = False):
    while np > 0:
        parent = (np-1)//2
        if is_min and nums[parent] <= nums[np]:
            return nums
        
        if not is_min and nums[parent] >= nums[np]:
            return nums
        
        nums[parent], nums[np] = nums[np], nums[parent]
        np = parent
    return nums

def insert_min(nums):
    arr = []

    for i in nums:
        arr.append(i)
        arr = bubble(arr, len(arr)-1, True)
    
    return arr

def insert_max(nums):
    arr = []

    for i in nums:
        arr.append(i)
        arr = bubble(arr, len(arr) - 1)
    
    return arr

# Review
def shift_down(nums, is_min = False):
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left > len(nums) or right > len(nums):
        return nums

    if is_min:
        if nums[i] <= nums[left] and nums[i] <= nums[right]:
            return nums

        min = i
        if left < len(nums) -1 and nums[i] > nums[left]:
            min = left
        
        if right < len(nums) - 1 and nums[i] > nums[right]:
            min = right
        
        if min != i:
            nums[min], nums[i] = nums[i], nums[min]
        
        i = min

    return shift_down(nums, i, is_min)

def delete_min(arr, i):
    # some
    if not arr:
        return None
    
    # Update with last element
    first_elem = arr[i]
    arr[i] = arr[-1]
    arr.pop()

    while i <= len(arr) - 1:
        left = i * 2 + 1
        right = i * 2 + 2

        min = i
        if left < len(arr) and arr[min] > arr[left]:
            min = left
        
        if right < len(arr) and arr[min] > arr[right]:
            min = right

        if i == min:
            break

        arr[min], arr[i] = arr[i], arr[min]
        i = min
        
    return first_elem


arr = insert_min(nums)
print("MinHeap: ", arr)
# arr = insert_max(nums)
# print("MaxHeap: ", arr)
# arr = delete_min(arr, 0)
# print("Deleted: ", arr)

hp = []

while arr:
    hp.append(delete_min(arr, 0))

print(hp)

# arr = min_heap(nums)
# print("Min Heap", arr)

# arr = min_heap(nums)
# print("Max Heap", arr)


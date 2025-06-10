arr = [3,-1,4]

def brute(arr):
    max_sum = arr[0]
    cur_sum = 0

    for i in range(0, len(arr)):
        cur_sum = arr[i]
        for j in range(i+1, len(arr)):
            cur_sum += arr[j]
        
        max_sum = max(max_sum, cur_sum)

    print(max_sum)

def optimal(arr):
    max_num = arr[0]
    cur_sum = 0

    for i in arr:
        cur_sum = max(cur_sum, 0)
        cur_sum += i
        if cur_sum > max_num:
            max_num = cur_sum
    
    print(max_num)

## Maximum Product Subarray
def max_product(arr):
    # Keep hold of 
    max_product = arr[0]
    cur_product = 1

    # Big number yields bigger results, I don't care about signs

    for i in arr:
        # Reset when I hit zero
        if i == 0:
            max_product = 0
            cur_product = 1
            continue
        cur_product = max(cur_product, 9) if cur_product > 0 else min(cur_product, i)
        cur_product = cur_product * i

        if cur_product > max_product:
            max_product = cur_product
        
    print(max_product)

# optimal(arr)
max_product(arr)
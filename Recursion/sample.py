nums = [76,23,10,78,16]

def divisible(nums):
    if not nums:
        return 0

    if nums[0] % 5 ==0:
        return nums[0]
    
    print("Printing ", nums[0])
    num = recursion(nums[1:])
    print(num)

#divisible(nums)

def add(n, i,sum):
    if i == n:
        return sum + i

    sum = add(n,i+1,sum)
    print(sum)
    return sum + i


def factorial(n,num):
    if n==0:
        return 1

    num = factorial(n-1,num) 
    return num * 1

#print(factorial(5,1))

#n = add(5,1,0)
#print(n)

def fibonacci(n):
    pass


x = 2.00
n=-2

def pow(x,n):
    print("N: ", n)
    if n==0:
        return 1
    
    is_neg = n < 0
    # Solve n/2 half and supply

    if is_neg:
        x = (1/x)
        n = -n
    
    half = pow(x,n//2)

    # for odd number the number gets left out
    if n % 2 ==0:
        return half * half

    return half * half * x


print(f"Before : {x}")
val = pow(x,n)
print(f"After: {val}")

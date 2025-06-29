x = 2.00
n=-20

def pow(x,n):
    print("N: ", n)
    if n==0:
        return 1
    
    is_neg = n < 0
    
    # Solve n/2 half and supply

    if is_neg:
        return (1/x) * pow(x,n+1)

    return x * pow(x,n-1)


print(f"Before : {x}")
val = pow(x,n)
print(f"After: {val}")

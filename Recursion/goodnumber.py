import math

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def is_even(n):
    return n % 2 == 0


def get_good(s, i=0):
    if not s:
        return True

    val = int(s[0])
    if (is_even(i) and is_even(val)) or (not is_even(i) and is_prime(val)):
        return get_good(s[1:], i+1)

    return False

import time
def all_good(n,tot = 0):
    if n == 0:
        return 1

    print(n)
    time.sleep(0.005)
    tot = all_good(n-1, tot)
    if get_good(str(n)):
        tot += 1
    print(n, get_good(str(n)), tot)
    return tot
    

n=4
print(all_good(10**n))

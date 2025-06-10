"""
https://leetcode.com/problems/missing-number/
start: Feb 25
end: Feb 26
revision:
"""

n = 5
series = [1,0,3]

# loop until n 
# inner loop check i is present in j
def two_loop(n,series):
    k = 0

    for i in range(n):
        k = i
        for j in range(len(series)):
            if series[j] == i:
                k=0
                break
        
        if k > 0:
            break
    
    return k

def hashway(n,series):
    hsh = {}

    for i in range(1, n+1):
        hsh[i] = 0
    
    for i in series:
        hsh[i] += 1

    for i in hsh:
        if hsh[i] == 0:
            return i

    return -1

def xor(n, series):
    sum1 = 0
    for i in range(n+1):
        sum1 = sum1 ^ i
    
    for i in series:
        sum1 = sum1 ^ i
    
    return sum1

# Summation of range
# Summation of given series
# subract to get the missing
def optimal(n, series):

    sum1 = 0
    # Len of series is tricky
    for i in range(len(series)+1):
        sum1 += i
    
    sum2 = 0
    for i in series:
        sum2 += i

    print(sum1, sum2)
    return sum1 - sum2

if __name__ == "__main__":
    # print(hashway(5, series))
    print(xor(5, series))
    print(optimal(5, series))
    # print(3 ^ 2)

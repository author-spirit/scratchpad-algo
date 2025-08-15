
memo = {}

"""
With usage of memoization we reduced O(2^n) times to O(n) times
Basics of DP: Solving overlapping subproblems by storing the state
Memoization: Hash..
Tabulation: Keep track of sum in array
constantspace: Keep track of states in variables similar to 2 pointers
"""
def constant_space(n):
    if n== 1 or n==2:
        return n

    prev = 1
    cur = 2
    
    for i in range(2,n):
        _prev = prev
        prev = cur
        cur = _prev + cur
        #prev,cur = cur, prev+cur

    return cur 

def tabulation(n):
    if n == 1 or n == 2:
        return n
    
    tab = [0] * n
    tab[0] = 1
    tab[1] = 2
    
    for i in range(2,n):
        tab[i] = tab[i-2] + tab[i-1]
    
    return tab[-1] 

def backtrack(n):
    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = backtrack(n-1) + backtrack(n-2)
    return memo[n]

print("Memoization -> ", backtrack(4))
print("Tabulation -> ", tabulation(4))
print("Constant Space -> ", constant_space(4))

n=4

"""
Requires Backtracking
Below is bruteforce
"""

def backtracking():
    for i in range(2**n):
        s = str(format(i,f'0{n}b'))
        if '00' in s:
            continue
        print(s)

subsets = []
def optimal(i,subset):
    if i == n-1:
        subsets.append(subset)
        return
    
    # include red
    optimal(i+1, subset + '1')

    # Not Include
    if not subset or subset[-1] != '0':
        optimal(i+1,subset+'0')
    

optimal(0,'')
print(subsets)

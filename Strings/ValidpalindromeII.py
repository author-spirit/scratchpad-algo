"""
URL: https://leetcode.com/problems/valid-palindrome-ii/
Intuition: Every palindrome has one common pattern i.e. 1st and last
           character are same. No eliminate N-2/2nd character,
           reverse and compare with clean string.
"""

# Loose way
def valid_palindrome(s):
    if len(s)==1:
        return False

    clean = s[:len(s)-2] + s[-1]
    print(clean, clean[::-1])
    return clean == clean[::-1]

# Fail-safe
def valid(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0)+1

    min = ""
    for (char, count) in freq.items():
        if freq.get(min, float('inf')) > count:
            min = char
    print("min:", min)

    clean = ""
    for c in s:
        if c != min:
            clean+=c
    
    print(clean)
    return clean == clean[::-1]

def simple(s):
    l=0
    r=len(s)-1

    is_palin = True
    while l <= r:
        if s[l] != s[r]:
            if is_palin:
                is_palin = False
            else:
                return False
        l+=1
        r-=1
    print(l,r)
    return l != r
s = "abc"
#print(s)
print(s,simple(s))

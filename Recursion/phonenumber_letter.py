"""
Ref: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

digits = '23'
keypad = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
n=len(digits)
subsets = []
sub=[]
def backtrack(i):
    if i == n:
        subsets.append(''.join(sub))
        return

    digit = keypad[digits[i]]
    for d in digit:
        sub.append(d)
        backtrack(i+1)
        sub.pop()
    return subsets

sbs = backtrack(0)
print(sbs)

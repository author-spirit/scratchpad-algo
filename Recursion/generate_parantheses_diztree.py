"""
Semi-Optimal Solution
Ref: https://leetcode.com/problems/generate-parentheses/
"""

n = 4
subs = []

def is_valid(s):
    stack = [s[0]] 
    i=1
    while i < len(s):
        if not stack:
            stack.append(s[i])
        elif s[i] == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s[i])
        i+=1
    print("Stack", s,stack)
    return len(stack) == 0


from sys import *
def backtrack(s):
    if len(s) == n*2:
        #print(s, is_valid(s))
        if is_valid(s):
            subs.append(s)
        return
    
    backtrack(s+'(')
    
    # exclude
    backtrack(s+')')

backtrack('')
print(subs)

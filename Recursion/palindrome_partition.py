"""
Ref: https://leetcode.com/problems/palindrome-partitioning/description/
"""

s = "aab"

parts = []
n = len(s)
def backtracking(idx, part):
    if idx >= n:
        parts.append(part.copy())
        return
    
    for sidx in range(idx, n):
        char = s[idx:sidx+1]
        if char == char[::-1]:
            part.append(char)
            backtracking(sidx+1,part)
            part.pop()

backtracking(0,[])
print(parts)

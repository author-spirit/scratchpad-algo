n=3
arr = [1,2,2]

sums = []
def backtrack(i,sum):
    if i==n:
        sums.append(sum)
        return 

    backtrack(i+1,sum+arr[i])
    backtrack(i+1,sum)

backtrack(0,0)
sums.sort()
print(set(sums))

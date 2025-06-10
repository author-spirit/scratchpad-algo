# Mar 31 2025

arr = [1,2,6,2,4,1]
mx = 0

win = 3

# Get the sum of first "win" values
# Like Gamification:
# Minus the value in previous left pointer
# Add the value in right pointer

for i in range(win):
    mx += arr[i]

i=1
j=win

while j < len(arr):
    val = (mx - arr[i-1]) + arr[j]
    if val > mx:
        mx = val
    
    i += 1
    j += 1

print(mx)
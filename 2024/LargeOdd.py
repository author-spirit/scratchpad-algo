nums = "60"

high = ""
for c in nums:
    if int(c) % 2 != 0:
        high += c

print(high)
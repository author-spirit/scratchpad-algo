strs = ["flower","some"]

words = sorted(strs)
print(words)

freq = ""
for i in range(min(len(words[0]), len(words[-1]))):
    if words[0][i] == words[-1][i]:
        freq += words[0][i]
    else:
        break

print(freq)

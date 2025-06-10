s = "0P"

text = ""
text2 = ""
for c in s.lower():
    if c.isalnum():
        text += c
        text2 = c + text2

print(text, text2)

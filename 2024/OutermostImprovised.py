# Green - My Thought

parentheses = "()(())"

i = 0
new_string = ""

for c in parentheses:
    if c == '(':
        if i > 0:
            new_string = new_string + c
        i = i + 1
    
    if c == ')':
        i = i - 1
        if i > 0:
            new_string = new_string + c
    
    print(i)

print(new_string)
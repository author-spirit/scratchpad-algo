# Green - My Thought

parentheses = "()()"

start = 0
end = 0
new_string = ""

for c in parentheses:
    if c == '(':
        if start > 0:
            new_string = new_string + c
        start = start + 1
    
    if c == ')':
        if (end + 1) < start:
            new_string = new_string + c
            end = end + 1
        else:
            start = end = 0

print(new_string)
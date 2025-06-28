s='0-1'

def atoi(s, prev=None):
    if not s:
        return ''
    
    val = s[0]

    if val in ['-', '+'] and not prev:
        return val + atoi(s[1:], val)

    if val in ['-', '+'] and prev:
        return atoi(s[1:], val)

    if val.strip() in ['','=','_']:
        return atoi(s[1:])

    if val.isalpha():
        if not prev:
            return atoi(s[1:])
        return ''
    
    print(val, prev)
    return val + atoi(s[1:], val)

print(f"Before: {s}")
val = atoi(s)
print(f"After: {int(val)}")

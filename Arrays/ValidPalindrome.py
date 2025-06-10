s = "."

def version1(s):

    i=0
    j=len(s)-1
    is_valid = False

    print(i, j)

    while i < j:
        if not (ord(s[i]) >= 65 and ord(s[i]) <= 122):
            i += 1
            continue
        
        if not (ord(s[j]) >= 65 and ord(s[j]) <= 122):
            j -= 1
            continue
        
        if s[i].lower() != s[j].lower():
            return False
        
        if not is_valid:
            is_valid = True
        
        i += 1
        j -= 1
    
    return is_valid


def version2(s):
    clean = ""

    for c in s:
        if ord(c) >= 65 and ord(c) <= 122:
            clean += c.lower()

    i=0
    j=len(clean)-1
    is_valid = False

    while i < j:
        if clean[i] != clean[j]:
            is_valid = False
            break
        
        if not is_valid:
            is_valid = True
        
        i += 1
        j -= 1
    
    return is_valid
    
# print(version1(s))

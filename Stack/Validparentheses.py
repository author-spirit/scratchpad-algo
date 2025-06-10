s = "()[]{}"

def check(s):
    stack = []
    for i in s:
        curr = i
        if curr in ['(','{', '[']:
            stack.append(curr)
            continue

        prev = '' if not stack else stack.pop()
        if (curr == ')' and prev!='(') \
            or (curr == ']' and prev != '[') \
            or (curr == '}' and prev != '{'):
            return False
    # Check whether remaining elements exists in stack
    # if yes then parentheses not ended properly
    # if no, then properly ended
    return len(stack) == 0


#import sys
#sys.exit()
series = ["()[]{}", "(]", "()", "([.)","([])", "([})", "([{}])","([{([{{{}}}])}])", '{}', '{\}', '((', '{']
for s in series:
    print(s, check(s))

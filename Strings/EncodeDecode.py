def encode(strs):
    
    txt = ""
    for i in strs:
        txt += str(len(i)) + "!" + i
    return txt

def decode(txt):

    arr = []
    i = 0

    while i < len(txt):
        j = i
        num = ""

        # extract the number
        while j < len(txt) and txt[j] != "!":
            num += txt[j]
            j += 1

        # 7!,samsung
        range_len = i + len(num) + 1
        sub = txt[range_len: range_len + int(num)]
        arr.append(sub)
        i = range_len + len(sub)

    return arr

strs = ["6!samsung","apple","sony","hewlettpackard"]
txt = encode(strs)
print(txt)
arr = decode(txt)

assert arr == strs, "not equal"

# LC: https://leetcode.com/problems/reverse-words-in-a-string/
# revisit: Mar 8, 2024

def brute(s):
    word = ""
    nw = ""
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            word = s[i] + word
        
        if word != "":
            if (i > 0 and s[i] == ' ' and s[i-1] != ' '):
                    nw += word + " "
                    word = ""
            if i == 0:
                    nw += word
                    word = ""

    print("("+nw+ ")") 

def optimal(s):
    print(" ".join(filter(lambda a:a.strip(), s.split(" ")[::-1])))

optimal("  hellow world  ")
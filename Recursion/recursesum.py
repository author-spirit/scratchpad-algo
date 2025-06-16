def sum(a,i=0):
    if(i == len(a)):
        return 0
    
    return a[i] + sum(a, i+1)

a = [10,30,40]
print(sum(a))

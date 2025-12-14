
# LAMBDA: A lambda function can take any number of arguments, but can only have one expression.S

sqr = lambda n: n ** 2
print(sqr(2))

mul = lambda a,b: a*b
print(mul(2,3))

def operation(n):
    return lambda m: f'{n} x {m}'

op = operation(2)
print(op(3))

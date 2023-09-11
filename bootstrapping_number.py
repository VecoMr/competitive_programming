import math

n = int(input())

def f(x):
    return n**(1/x)-x

def fprime(x):
    return -1 -(((n**(1/x))*math.log(n))/x**2)

a = 1
b = a - f(a)/fprime(a)

def isgood(a, b):
    r = ""
    for i, j in zip(str(a), str(b)):
        if i == j:
            r += i
        else:
            break
    return r

for i in range(1000):
    t = b
    b = a - f(a)/fprime(a)
    a = t


print(b)
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

for i in open(0):
    l = list(map(int, i.split()))
    res = 1
    for i in l:
        res = lcm(res, i)
    print(res)
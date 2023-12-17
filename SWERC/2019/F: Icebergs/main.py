import math
 
n = int(input())

def calc_tri(a, b, c):
    tmp = (a+b+c)/2
    return (tmp * (tmp - a) * (tmp - b) * (tmp - c))**0.5

def dist(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

res = 0
for _ in range(n):
    m = int(input())
    first = list(map(int, input().split()))
    tmp = first
    for _ in range(m-1):
        c = list(map(int, input().split()))
        res += (tmp[0] - c[0]) * ((tmp[1] + c[1]) / 2)
        tmp = c

    res += (tmp[0] - first[0]) * ((tmp[1] + first[1]) / 2)

print(abs(res))


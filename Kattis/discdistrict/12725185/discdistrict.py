import math

n = int(input())

x = n
y = 0

m = math.inf
mx = -1
my = -1


def calc(x:int, y:int) -> float:
    return (x * x + y * y) ** 0.5

t = calc(x, y)
while y != n:
    if n < t:
        if m > t:
            m = t
            mx = x
            my = y
    a = calc(x-1, y)
    b = calc(x, y+1)
    if a < n:
        t = b
        y += 1
    elif b < n:
        t = a
        x -= 1
    elif a < b:
        t = a
        x -= 1
    else:
        t = b
        y += 1
print(mx, my)
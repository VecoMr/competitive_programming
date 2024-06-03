import math

n = int(input())

for _ in range(n):
    m = int(input())
    l = [input() for _ in range(m)]
    x, y = 0, 0
    dir = 90
    for i in l:
        a, v = i.split()
        v = int(v)
        if a == 'fd':
            x += math.cos(math.radians(dir)) * v
            y += math.sin(math.radians(dir)) * v
        elif a == 'bk':
            x -= math.cos(math.radians(dir)) * v
            y -= math.sin(math.radians(dir)) * v
        elif a == 'lt':
            dir = (dir + v) % 360
        elif a == 'rt':
            dir = (dir - v) % 360
    d = round(math.sqrt(x**2 + y**2))
    print(d)